<template>
  <v-card flat>
    <v-card-title v-if="!Viewport">
      <v-avatar class="mr-2" size="2.625rem">
        <v-img :src="post.author.avatar"></v-img>
      </v-avatar>

      <v-card-subtitle class="pa-0">
        <router-link class="subtitle-1 font-weight-bold" v-text="post.author.nickname" :to="{ path: `/user/${post.author.id}/index` }"></router-link>
        <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
        <span class="d-flex caption grey--text">
          <span class="mr-1">
            {{ post.timestamp | format }}
          </span>
          <span v-if="post.author.location">
            <v-icon size="14" class="grey--text">mdi-map-marker</v-icon>
            {{ post.author.location }}
          </span>
        </span>
      </v-card-subtitle>
    
      <div class="flex-grow-1"></div>
      <v-btn small icon @click="show = !show">
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-title>

    <v-card-text class="pa-0 px-sm-4 pl-sm-10">
      <core-box-image class="pl-sm-6 pr-sm-3" :post="post"></core-box-image>
      <core-box-actions v-if="Viewport" :post="post" class="caption text-truncate"></core-box-actions>
      <core-box-md-actions v-if="!Viewport" :post="post" class="caption text-truncate px-2 pl-sm-6"></core-box-md-actions>
    </v-card-text>
  </v-card>
</template>

<script>
import { format } from '@/utils'

export default {
  props:{
    post: [Object,Array],
    n: [Number, String]
  },
  data() {
    return {
      show: false,
      active: false,
      amenities: true,
      width: null,
      Viewport: null
    }
  },
  created() {
    this.viewBreak()
  },
  filters: {
    format: function (params) {
      return format(params)
    }
  },
  methods: {
    viewBreak() {
      window.innerWidth < 600 ? this.Viewport = true : this.Viewport = false
      return this.width = window.innerWidth
    }
  },
  mounted() {
    window.addEventListener("resize", this.viewBreak)
  },
}
</script>

