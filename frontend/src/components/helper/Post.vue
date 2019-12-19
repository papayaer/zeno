<template>
  <v-card class="mb-4">
    <v-img v-if="post.img" class="align-end white--text"
      :src='post.img'>
      <v-card-actions class="caption justify-end">
        <v-btn text icon small><v-icon size="18" color="red">mdi-heart</v-icon></v-btn>
        <span>{{post.favorite_count}}</span>
      </v-card-actions>
    </v-img>
    
    <v-card-title v-if="post.title" class="text-truncate title" v-html="post.title"></v-card-title>
    <v-card-text class="text-truncate grey--text" v-html="post.body"></v-card-text>

    <v-divider></v-divider>

    <core-box-actions :post="post"></core-box-actions>
  </v-card>
</template>

<script>
export default {
  props:{
    post: [Object,Array]
  },
  created() {
    this.body()
    this.title()
    this.hasImg()
  },
  methods: {
    body() {
      this.post.body.length <= '120' ? this.post.body : this.post.body.slice(0,120)+' ....'
    },
    title() {
      if (this.post.title) {
        this.post.title.length <= '60' ? this.post.title : this.post.title.slice(0,60)+' ....'
      }
    },
    hasImg() {
      if (!this.post.img) {
        this.post.img = 'https://picsum.photos/450/540?image='+ this.post.id/5*10
      }
    }
  }
}
</script>

