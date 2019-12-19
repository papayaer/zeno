<template>
  <v-speed-dial bottom right open-on-hover fixed v-model="fab"
    transition="slide-y-reverse-transition">
    <template v-slot:activator>
      <v-btn dark fab v-model="fab" color="primary">
        <v-icon v-if="fab">mdi-close</v-icon>
        <v-icon v-else>mdi-account-circle</v-icon>
      </v-btn>
    </template>
    <v-btn fab dark small color="indigo">
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-btn fab dark small color="green" v-if="isLogin" :to="{ path: `/user/${$store.state.currentUser.id}/writepost` }">
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
    <v-btn fab dark small color="red" v-if="isLogin" @click="logout">
      退出
    </v-btn>
  </v-speed-dial>
</template>


<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      fab: false
    }
  },
  computed: {
    ...mapState([
      'isLogin'
    ])
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  },
}
</script>