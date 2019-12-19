<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">动态</v-col>
    
    <v-col v-if="!article.length" cols="12">
      <v-skeleton-loader
        transition="fade-transition"
        height="100%"
        type="article"
      ></v-skeleton-loader>
    </v-col>

    <v-col v-else cols="12" v-for="(item, index) in article" :key="index">
      <core-card-media
        :post="item"
        :downtitle="true">
        <template v-slot:by>发布</template>
      </core-card-media>
    </v-col>

    <v-col cols="12" class="mx-auto text-center">
      <v-btn v-if="!loadmsg" text rounded width="160" :disabled="loading" @click="fetchPost">
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
import { followedPost } from '@/api/users'

export default {
  data() {
    return {
      loading: false,
      article: [],
      page: 1,
      loadmsg: null
    }
  },
  created() {
    this.fetchPost()
  },
  watch: {
    '$route': 'fetchPost'
  },
  methods: {
    async fetchPost () {
      this.loading = true
      await followedPost(this.page, this.$route.params.author)
        .then(re => {
          this.loading = false
          re.data.next ? this.page ++ : this.loadmsg = '没有了'
          this.article = this.article.concat(re.data.posts)
        })
    }
  }
}
</script>