// https://vuex.vuejs.org/en/actions.html

import {authentication, register, ref_user_info} from '@/api/authentication'

export default {
  hasDialog(context){
    return context.commit('setDalog')
  },

  login(context, userData) {
    return authentication(userData)
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
  },

  async doRegister(context, userData) {
    await register(userData)
          .then(() => context.dispatch('login', userData))
  },

  logout (context) {
    context.commit('setLogout')
  },

  relogin(context, userData) {
    return context.commit('setCurrentUser', userData)
    // console.log(userData)
  },

  ref(context, author) {
    return ref_user_info(author)
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
  },

  currentPost(context, postData){
    return context.commit('setTitle', postData)
  }
}
