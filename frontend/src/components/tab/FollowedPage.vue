<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">{{ follower }}的关注</v-col>

    <v-col v-if="!followeds.length" cols="12">
      <v-skeleton-loader
        transition="fade-transition"
        height="100%"
        type="article"
      ></v-skeleton-loader>
    </v-col>

    <v-col v-else cols="12" class="py-1 py-md-2">
      <v-card outlined class="v-card--shadow">
        <template v-for="(item, i, k) in followeds">
          <core-fans :item="item" :avatar='i' :key="i"></core-fans>
          <v-divider v-if="i + 1 < followeds.length" :key="k"></v-divider>
        </template>
      </v-card>
    </v-col>

    <v-col cols="12" class="mx-auto text-center">
      <v-btn v-if="!loadmsg" text rounded width="160" :disabled="loading" @click="get_followed">
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
import { followed } from '@/api/follows'

export default {
  props: {  // 路由传的参(author_id)
    author: {
      type: String,
      default: '1'
    }
  },
  data() {
    return {
      follower: null,
      loading: false,
      followeds: [],
      page: 1,
      loadmsg: null
    }
  },
  created() {
    this.get_followed()
  }, 
  methods: {
    async get_followed() {
      this.loading = true
      await followed(this.page, this.author)
        .then(re => {
          this.loading = false
          re.data.next ? this.page ++ : this.loadmsg = '没有了'
          this.followeds = this.followeds.concat(re.data.followed)
          this.followeds = re.data.followed
          this.follower = re.data.follower
        })
    }
  },
}
</script>