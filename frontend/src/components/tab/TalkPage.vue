<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">{{ nickname }}参与的讨论</v-col>

    <v-col v-if="!comments.length" cols="12">
      <v-skeleton-loader
        transition="fade-transition"
        height="100%"
        type="article"
      ></v-skeleton-loader>
    </v-col>

    <v-col v-else cols="12" class="py-1 py-md-2">
      <v-card outlined class="v-card--shadow">
        <template v-for="(item, i, k) in comments">
          <core-talk :item="item" :key="i"></core-talk>
          <v-divider v-if="i + 1 < comments.length" :key="k"></v-divider>
        </template>
      </v-card>
    </v-col>

    <v-col cols="12" class="mx-auto text-center">
      <v-btn v-if="!loadmsg" text rounded width="160" :disabled="loading" @click="get_comment">
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
import { comment } from '@/api/comments'

export default {
  props: {  // 路由传的参(author_id)
    author: {
      type: String,
      default: '1'
    }
  },
  data() {
    return {
      nickname: null,
      loading: false,
      comments: [],
      page: 1,
      loadmsg: null
    }
  },
  created() {
    this.get_comment()
  }, 
  methods: {
    async get_comment() {
      this.loading = true
      await comment(this.page, this.author)
        .then(re => {
          this.loading = false
          re.data.next ? this.page ++ : this.loadmsg = '没有了'
          this.comments = this.comments.concat(re.data.comments)
          this.nickname = re.data.user
        })
    }
  },
}
</script>