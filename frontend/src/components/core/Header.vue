<template>
  <v-list-item>
    <v-list-item-avatar color="grey" class="my-0 ml-0 mr-2">
      <v-img :src="post.author.avatar"></v-img>
    </v-list-item-avatar>
    <v-list-item-content class="py-0">
      <v-list-item-title class="align-self-start subtitle-2 font-weight-bold">
        <router-link v-text="post.author.nickname" :to="{ path: `/user/${post.author.id}/index` }"></router-link>
        <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
        <span class="caption grey--text">{{ post.author.location }}</span>
      </v-list-item-title>
      <v-list-item-subtitle class="caption grey--text">
        {{ timestamp }}
      </v-list-item-subtitle>
    </v-list-item-content>
    <v-list-item-action v-if="post.author.id==$store.state.currentUser.id" class="align-self-start my-0 ml-2 caption grey--text">
      <v-btn small icon class="mx-1">
        <svg t="1574216577856" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3022" width="18" height="18"><path d="M862.709333 116.042667a32 32 0 1 1 45.248 45.248L455.445333 613.813333a32 32 0 1 1-45.258666-45.258666L862.709333 116.053333zM853.333333 448a32 32 0 0 1 64 0v352c0 64.8-52.533333 117.333333-117.333333 117.333333H224c-64.8 0-117.333333-52.533333-117.333333-117.333333V224c0-64.8 52.533333-117.333333 117.333333-117.333333h341.333333a32 32 0 0 1 0 64H224a53.333333 53.333333 0 0 0-53.333333 53.333333v576a53.333333 53.333333 0 0 0 53.333333 53.333333h576a53.333333 53.333333 0 0 0 53.333333-53.333333V448z" fill="grey" p-id="3023"></path></svg>
      </v-btn>
    </v-list-item-action>
    <v-list-item-action v-else class="align-self-start my-0 ml-2">
      <btn-favorite :post="post"></btn-favorite>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
import {format} from '@/utils'

export default {
  props:{
    post: [Object,Array]
  },
  computed: {
    timestamp() {
      return this.post.timestamp = format(this.post.timestamp)
    }
  }
}
</script>