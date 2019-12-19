<template>
  <v-app-bar app elevate-on-scroll  v-scroll="onScroll" :class="[scroll?color:'transparent']">
    <div class="nav-bar d-flex align-center" style="width:100%;height:100%;">
      <!-- <v-toolbar-title class="headline text-uppercase mr-4">
        <v-icon color="primary">mdi-camera</v-icon>
      </v-toolbar-title> -->
      <v-img width="203px" max-width="60%" class="shrink" src="/assets/img/alpha-logo.png"></v-img>

      

      <div class="flex-grow-1"></div>
      <v-btn text to="/" active-class="active-class--home">首页</v-btn>
      <v-btn text to="/explore" class="mx-1" active-class="active-class--explore">浏览</v-btn>
      <v-btn text to="/activity" active-class="active-class--activity">话题</v-btn>
      <!-- <div class="v-responsive mr-0 hidden-xs-only" style="max-width:168px;">
        <div class="v-responsive__content">
          <v-text-field rounded flat solo dense
            label="搜索..."
            solo-inverted
            single-line
            hide-details
            prepend-inner-icon="mdi-magnify">
          </v-text-field>
        </div>
      </div> -->
      <!-- <div v-if="isLogin">
        <v-chip pill color="transparent" class="mx-md-3" :to="{ path: `/user/${$store.state.currentUser.id}/index` }">
          <v-avatar left>
            <v-img :src="currentUser.avatar"></v-img>
          </v-avatar>
          {{currentUser.nickname}}
        </v-chip>
      </div> -->
      <!-- <div v-else> -->
        <!-- <v-btn rounded depressed @click.stop="login" color="primary" class="mx-md-2">
          <v-icon left>mdi-account-circle</v-icon>登录
        </v-btn> -->
        <!-- <v-btn outlined class="mx-md-2 hidden-xs-only" color="primary" to=/user/register>
          <v-icon left>mdi-account-circle</v-icon>注册
        </v-btn> -->
      <!-- </div> -->
    </div>

    <div v-if="$route.name == 'single'" class="bar-post-title d-flex align-center justify-center">
      <v-container class="container-xl py-0">
        <v-row no-gutters justify="center" v-if="currentPost && currentPost.author">
          <v-col lg="7" md="7" sm="9" cols="8" class="d-flex px-md-3 align-center">
            <h1 class="pl-md-4 text-truncate">{{ currentPost.title }}</h1>
            <!-- <v-btn small outlined icon color="grey">
              <svg t="1574212106279" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4195" width="18" height="18"><path d="M335.008 916.629333c-35.914667 22.314667-82.88 10.773333-104.693333-25.557333a77.333333 77.333333 0 0 1-8.96-57.429333l46.485333-198.24a13.141333 13.141333 0 0 0-4.021333-12.864l-152.16-132.586667c-31.605333-27.52-35.253333-75.648-8.234667-107.733333a75.68 75.68 0 0 1 51.733333-26.752L354.848 339.2c4.352-0.362667 8.245333-3.232 10.026667-7.594667l76.938666-188.170666c16.032-39.2 60.618667-57.92 99.52-41.461334a76.309333 76.309333 0 0 1 40.832 41.461334l76.938667 188.16c1.781333 4.373333 5.674667 7.253333 10.026667 7.605333l199.712 16.277333c41.877333 3.413333 72.885333 40.458667 69.568 82.517334a76.938667 76.938667 0 0 1-26.08 51.978666l-152.16 132.586667c-3.541333 3.082667-5.141333 8.074667-4.021334 12.853333l46.485334 198.24c9.621333 41.013333-15.36 82.336-56.138667 92.224a75.285333 75.285333 0 0 1-57.525333-9.237333l-170.976-106.24a11.296 11.296 0 0 0-12.010667 0l-170.986667 106.24z" fill="#fb8c00" p-id="4196"></path></svg>
            </v-btn> -->
          </v-col>

          <v-col lg="3" md="3" sm="3" cols="4" class="d-flex align-center justify-center px-md-3">
            <v-avatar left size="35" class="mx-2">
              <img :src="currentPost.author.avatar">
            </v-avatar>
            <h3 class="text-truncate">
              <router-link v-text="currentPost.author.nickname" :to="{ path: `/user/${currentPost.author.id}/index` }"></router-link>
            </h3>
            <core-follow :user="currentPost.author" class="ml-2">+关注</core-follow>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      scroll: false,
      color: 'grey lighten-4'
    }
  },
  created() {
    this.reLogin()
  },
  computed: {
    ...mapState([
      'isLogin',
      'currentUser',
      'currentPost'
    ])
  },
  methods: {
    login() {
      if (this.isLogin) {
        this.logout()
      }
      this.$store.dispatch('hasDialog')
    },
    logout() {
      this.$store.dispatch('logout')
    },
    reLogin() {
      if (localStorage.getItem('token')) {
        if (this.$store.getters.expToken) {
          this.$store.dispatch('relogin', JSON.parse(localStorage.getItem('user')))
        }
      }
    },
    onScroll(e) {
      // console.log(e.currentTarget.scrollY)
      this.scroll = e.currentTarget.scrollY > 28
    }
  }
}
</script>
