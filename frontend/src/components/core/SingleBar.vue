<template>
<v-row no-gutters>
  <v-col cols="12" id="userinfo" class="pb-md-3">
    <v-card outlined class="v-card--shadow">
      <v-card-title class="px-2">
        <v-avatar class="mr-2">
          <img :src="item.author.avatar">
        </v-avatar>
        <h3>
          <router-link v-text="item.author.nickname" :to="{ path: '/user/'+item.author.id+'/index' }"></router-link>
        </h3>
        <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
        <core-follow :user="item.author"></core-follow>
      </v-card-title>
      <v-card-subtitle class="pa-2">
        {{ item.author.bio }}
      </v-card-subtitle>
      <v-card-actions class="caption grey--text justify-space-between">
        <div class="d-inline-flex">关注<span class="ml-1">{{ item.author.followed_count }}</span></div>
        <div class="d-inline-flex">粉丝<span class="ml-1">{{ item.author.follower_count }}</span></div>
        <div class="d-inline-flex">文章<span class="ml-1">{{ item.author.post_count }}</span></div>
        <div class="d-inline-flex">讨论<span class="ml-1">{{ item.author.comment_count }}</span></div>
        <div class="d-inline-flex">收藏<span class="ml-1">{{ item.author.favorite_count }}</span></div>
      </v-card-actions>
    </v-card>
  </v-col>

  <v-col cols="12" class="pb-md-3">
    <v-card outlined class="v-card--shadow">
      <v-img class="white--text"
        src="https://picsum.photos/300/200"
        height="116"
        max-height="116"
        :aspect-ratio="16/9">
        <v-card-title>要让荤食者也喜爱素食</v-card-title>
        <v-card-actions class="justify-end">Listen Now</v-card-actions>
      </v-img>
    </v-card>
  </v-col>
  
  <v-col cols="12" class="pb-md-3">
    <v-card outlined class="v-card--shadow">
      <v-card-title class="pa-2 justify-space-between">
        <strong class="pl-3 body-1" style="border-left:4px solid #f5365c">
          读过
        </strong>
        <router-link class="caption grey--text right" to="">更多</router-link>
      </v-card-title>
      <v-card-text class="text-left justify-start">
        <v-avatar
          size="35"
          class="ma-1"
          v-for="(n, i) in 18" :key="i">
          <v-img :src="`https://randomuser.me/portraits/women/${n}.jpg`"></v-img>
        </v-avatar>
      </v-card-text>
    </v-card>
  </v-col>
</v-row>
</template>

<script>
export default {
  props:{
    item: [Object,Array],
    default: null
  },
}
</script>