<template>
  <v-row>
    <v-col v-if="!article.length" cols="12">
      <v-row>
        <v-col sm="6" cols="12" v-for="(item, index) in 2" :key="index">
          <v-skeleton-loader
          transition="fade-transition"
          height="100%"
          type="image"
          ></v-skeleton-loader>
        </v-col>
      </v-row>
    </v-col>
    <v-col v-else sm="6" cols="12" v-for="(item, index) in article" :key="index">
      <core-feed-card :height="350" :value="item" :img="img[index]"></core-feed-card>
    </v-col>
  </v-row>
</template>

<script>
import { article } from '@/api/posts'

export default {
  data() {
    return {
      article: [],
      img: ["moroccandays.jpg", "autumnclouds.jpg", "snowcup.jpg", "christmas.jpg", "july4.jpg", "firepots.jpg"],
      page: 1,
      loadmsg: ''
    }
  },
  created() {
    this.fetchPost()
  },
  methods: {
    async fetchPost() {
      await article(this.page)
        .then(re => {
          re.data.next ? this.page ++ : this.loadmsg = '到底了'
          this.article = this.article.concat(re.data.posts)
        })
    }
  }
}

</script>