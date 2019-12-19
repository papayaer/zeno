<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">收藏夹</v-col>

    <v-col v-if="!posts.length" cols="12">
      <v-skeleton-loader
        transition="fade-transition"
        height="100%"
        type="article"
      ></v-skeleton-loader>
    </v-col>

    <v-col v-else cols="12" v-for="(item, index) in posts" :key="index">
      <core-card-media
        :post="item.post"
        :imginfo="true"
        :downtitle="true">
        <template v-slot:by>收藏</template>
      </core-card-media>
    </v-col>
    
    <v-col cols="12" class="mx-auto text-center">
      <v-btn v-if="!loadmsg" text rounded width="160" :disabled="loading" @click="fetchFavorite">
        <span v-if="loading">
          正在努力加载
          <v-progress-circular
            indeterminate
            :size="18"
            :width="2"></v-progress-circular>
        </span>
        <span v-else>下一页</span>
      </v-btn>
      <span v-else>{{ loadmsg }}</span>
    </v-col>

  </v-row>
</template>

<script>
import { favoritePost } from '@/api/users'

export default {
  data() {
    return {
      loading: false,
      posts: [],
      page: 1,
      loadmsg: null
    }
  },
  created() {
    this.fetchFavorite()
  },
  methods: {
    async fetchFavorite() {
      this.loading = true
      await favoritePost(this.page, this.$route.params.author)
        .then(re => {
          this.loading = false
          re.data.next ? this.page ++ : this.loadmsg = '没有了'
          this.posts = this.posts.concat(re.data.posts)
        })
    }
  }
}
</script>