<template>
  <div class="py-3">
    <v-card-title class="subtitle-2 py-1 align-start">
      <v-avatar class="mr-2" size="40">
        <v-img :src="item.user.avatar"></v-img>
      </v-avatar>

      <div>
        <router-link :to="{ path: `/user/${item.user.id}/index` }">{{ item.user.nickname }}</router-link>
        <v-icon small class="mx-1" color="deep-orange">mdi-check-decagram</v-icon>
        <span class="caption grey--text">{{ item.user.location }}</span>
        <span class="d-flex caption grey--text">{{ timestamp }}</span>
      </div>
    
      <div class="flex-grow-1"></div>
      
      <core-btn-follow :user="item.user"></core-btn-follow>
    </v-card-title>

    <v-card-text class="pl-10 py-0">
      <div class="pl-6">
        <v-list-item-subtitle class="my-2 caption grey--text">
          <div class="d-inline-flex mr-4">关注<span class="ml-1">{{ item.user.followed_count }}</span></div>
          <div class="d-inline-flex mr-4">粉丝<span class="ml-1">{{ item.user.follower_count }}</span></div>
          <div class="d-inline-flex mr-4">文章<span class="ml-1">{{ item.user.post_count }}</span></div>
          <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{ item.user.comment_count }}</span></div>
          <div class="d-inline-flex mr-4">收藏<span class="ml-1">{{ item.user.favorite_count }}</span></div>
        </v-list-item-subtitle>
        <v-list-item-subtitle class="my-2 caption grey--text">
          {{ item.user.about_me }}
        </v-list-item-subtitle>
      </div>
    </v-card-text>
  </div>
</template>

<script>
import { format } from '@/utils'

export default {
  props: {
    item: {
      type: [Object, Array],
      default: null
    }
  },
  computed: {
    timestamp() {
      return this.item.timestamp = format(this.item.timestamp)
    }
  }
}
</script>