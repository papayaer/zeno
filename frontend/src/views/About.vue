<template>
  <v-row justify="center">
    <v-col v-if="!article.length" cols="12" style="max-width:680px;">
      <v-skeleton-loader
        transition="fade-transition"
        height="100%"
        type="card"
      ></v-skeleton-loader>
    </v-col>
    <v-col v-else cols="12" style="max-width:680px;"
      v-for="(item, index) in article" :key="index">
      <v-card flat hover class="v-card--shadow">
        <h3 class="text-center" style="height:16px;">
          <v-chip small color="primary" class="mt-n8">发布: {{ item.timestamp }}</v-chip>
        </h3>
        <v-card-text class="py-0">
          <v-img
            src="https://picsum.photos/400/220"
            gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)">
            <v-row no-gutters class="fill-height align-content-space-between">
              <v-col cols="12">
                <v-card-subtitle class="caption text-right">
                  <v-chip dark small class="text-uppercase">视频</v-chip>
                  <!-- <h3 class="title text-bgshadow white--text font-weight-bold mb-2">
                    {{ item.title }}
                  </h3> -->
                </v-card-subtitle>
              </v-col>
            </v-row>
          </v-img>
        </v-card-text>
        <v-card-title v-if="item.title" class="py-3 font-weight-bold">
          <router-link :to="{ path: `/post/${item.id}/single`}" v-text="item.title" ></router-link>
          <core-favorite :post="item"></core-favorite>
        </v-card-title>
        <v-card-text v-text="item.abstract"></v-card-text>
        <v-card-actions class="px-4 caption grey--text">
          <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{item.author.comment_count}}</span></div>
          <div class="d-inline-flex mr-4">收藏<span class="ml-1">{{item.author.favorite_count}}</span></div>
          <div class="flex-grow-1"></div>
          <v-avatar size="1.6rem" class="ml-n1"
            v-for="(n, i) in 6" :key="i">
            <img style="border: 2px solid #fff"
              :src="`https://randomuser.me/portraits/women/${n}.jpg`">
          </v-avatar>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { article } from '@/api/posts'

export default {
  data() {
    return {
      article: []
    }
  },
  beforeMount() {
    article()
      .then(re => { this.article = re.data.posts })
  },
}
</script>