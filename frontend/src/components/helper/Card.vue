<template>
  <v-card outlined class="v-card--shadow">
    <box-header :post="post" class="d-none d-md-flex py-2 px-4"></box-header>
    <v-card-text v-if="post.img" class="pa-0 px-md-4">
      <core-box-image :post="post"></core-box-image>
    </v-card-text>
    <v-card-text class="pa-2 px-md-4">
      <core-box-content class="markdown-body" :post="post"></core-box-content>
    </v-card-text>
    <v-divider class="mx-2 mx-md-4"></v-divider>
    <core-box-actions v-if="Viewport" :post="post" class="caption text-truncate"></core-box-actions>
    <core-box-md-actions v-if="!Viewport" :post="post" class="caption text-truncate px-2 px-md-4"></core-box-md-actions>
  </v-card>
</template>

<script>
export default {
  props:{
    post: [Object,Array],
    n: [Number, String]
  },
  data() {
    return {
      active: false,
      amenities: true,
      width: null,
      Viewport: null
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

