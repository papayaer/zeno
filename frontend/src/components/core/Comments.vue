<template>
  <div class="py-3">
    <v-card-title class="subtitle-2 py-1 align-start">
      <v-avatar class="mr-4" size="36">
        <v-img :src="item.author.avatar"></v-img>
      </v-avatar>

      <div>
        <router-link v-text="item.author.nickname" :to="{ path: `/user/${item.author.id}/index` }"></router-link>
        <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
        <span class="caption grey--text">{{ item.author.location }}</span>
        <span class="d-flex caption grey--text">{{ timestamp }}</span>
      </div>
    
      <div class="flex-grow-1"></div>
      <span class="caption">102</span>
      <v-icon small class="ml-1">mdi-thumb-up-outline</v-icon>
    </v-card-title>

    <v-card-text class="pl-sm-12 py-2">
      <div class="markdown-body pl-sm-6" v-html="item.comment_body"></div>
    </v-card-text>
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