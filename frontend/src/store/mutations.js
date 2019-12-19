// https://vuex.vuejs.org/en/mutations.html


export default {
  setDalog(state) {
    state.dialog = !state.dialog
  },

  setJwtToken(state, payload) {
    state.dialog = false
    state.jwt = payload.jwt.token
    localStorage.setItem("token", state.jwt)
    state.isLogin = true
    state.currentUser = payload.jwt.user
    localStorage.setItem("user", JSON.stringify(state.currentUser))
  },
  setLogout(state) {
    state.jwt = ''
    state.isLogin = false
    state.userData = ''
    state.currentUser = ''
    localStorage.removeItem("token")
    localStorage.removeItem("user")
  },
  setTitle(state, payload) {
    state.currentPost = payload
  },
  setCurrentUser(state, payload) {
    state.currentUser = payload
    state.isLogin = true
    // console.log(state.currentUser)
  }
}
