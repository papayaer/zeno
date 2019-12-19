<template>
  <div class="py-3">
    <v-card-title class="subtitle-2 py-1 align-start">
      <v-avatar class="mr-4" size="40">
        <v-img :src="item.author.avatar"></v-img>
      </v-avatar>

      <div>
        {{ item.author.nickname }}
        <v-icon small class="mx-1" color="deep-orange">mdi-check-decagram</v-icon>
        <span class="caption grey--text">{{ item.author.location }}</span>
        <span class="d-flex caption grey--text">{{ timestamp }}</span>
      </div>
    
      <div class="flex-grow-1"></div>
      <span class="caption">102</span>
      <v-icon small class="ml-1">mdi-thumb-up-outline</v-icon>
    </v-card-title>

    <v-card-text class="pl-sm-12 py-2">
      <div class="pl-sm-6">
        <v-card flat tile outlined color="#fbfbf9" style="border-color:none">
          <v-card-text class="text-center pa-1">
            <v-btn text small @click="show = !show">
              展开隐藏楼层
              <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-text>
        </v-card>
        <div class="py-1">{{ item.comment_body }}</div>
      </div>
    </v-card-text>

    <v-card-actions class="caption grey--text pl-sm-12">
      <div class="pl-2 pl-sm-6">
        <span><v-icon small class="mr-1">mdi-link</v-icon>原文: </span>
        <router-link :to="{ path: '/post/'+item.post_id+'/single/'}">{{ item.post_title }}...</router-link>
      </div>
    </v-card-actions>
  </div>
</template>

<script>
import {format} from '@/utils'

export default {
  props: {
    item: {
      type: [Object, Array],
      default: null
    }
  },
  data() {
    return {
      show: false
    }
  },
  computed: {
    timestamp() {
      return this.item.timestamp = format(this.item.timestamp)
    }
  }
}
</script>