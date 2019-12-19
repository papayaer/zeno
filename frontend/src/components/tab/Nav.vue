<template>
  <v-tabs show-arrows center-active slider-size="3" icons-and-text height="56">
    <v-tab v-for="(item, index) in tabs" :key="index" :to="{path: '/user/'+$route.params.author+'/'+item.href}">
      <h3 class="mb-0 text--primary">{{ item.counter() }}</h3>
      <span class="pt-1 caption grey--text">{{ item.name }}</span>
    </v-tab>
  </v-tabs>
</template>

<script>
import { author } from '@/api/users'

export default {
  data() {
    return {
      user: {},
      tabs:[
        {name: '动态', href: 'index', icon: 'mdi-home-outline', counter: () => this.user.index_count},
        {name: '关注', href: 'followed', icon: 'mdi-camera-outline', counter: () => this.user.followed_count},
        {name: '粉丝', href: 'fans', icon: 'mdi-camera-outline', counter: () => this.user.follower_count},
        {name: '收藏', href: 'favorite', icon: 'mdi-camera-outline', counter: ()=> this.user.favorite_count},
        {name: '讨论', href: 'talk', icon: 'mdi-camera-outline', counter: () => this.user.comment_count},
        {name: '历史', href: 'history', icon: 'mdi-bell-outline', counter: () => this.user.history_count},
        {name: '消息', href: 'messages', icon: 'mdi-bell-outline', counter: () => this.user.notifications_count}
      ]
    }
  },
  created() {
    this.navAuthor()
  },
  watch: {
    '$route':'navAuthor'
  },
  methods: {
    navAuthor() {
      author(this.$route.params.author)
      .then((response) => this.user = response.data)
    }
  },
}
</script>

