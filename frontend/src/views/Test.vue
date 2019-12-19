<template>
  <v-row justify="center">
    <v-col sm="8" md="7" cols="12">
      <v-card flat outlined class="v-card--shadow">
        <v-row no-gutters v-for="(item, index) in article" :key="index">
          <v-col sm="4" cols="5">
            <core-image class="pa-2 pa-sm-3" :post="imgarr"></core-image>
          </v-col>
          <v-col sm="8" cols="7">
            <v-card flat>
              <v-card-subtitle class="pb-0 grey--text">JUNE 26, 2008</v-card-subtitle>
              <v-card-title v-text="item.title" class="pt-0"></v-card-title>
              <v-card-subtitle class="grey--text">
                Cristian / Featured, Top Stories
              </v-card-subtitle>
              <v-card-text v-text="item.abstract"></v-card-text>
              <v-card-actions class="px-4 caption grey--text">
                <v-avatar size="1.36rem">
                  <img :src="item.author.avatar">
                </v-avatar>
                <span class="mx-2">{{ item.author.nickname }}</span>
                <div class="flex-grow-1"></div>
                <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{item.comment_count}}</span></div>
                <div class="d-inline-flex">收藏<span class="ml-1">{{item.favorite_count}}</span></div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
    <v-col sm="4" md="3" cols="12" class="pt-0">
      <core-right-bar></core-right-bar>
    </v-col>
  </v-row>
</template>

<script>
import {article} from '@/api/posts'

export default {
  data() {
    return {
      article: null,
      imgarr: ['http://p1.music.126.net/74o12RGkWOtAGRpiDaIZBQ==/109951164525127376.jpg?imageView&quality=89']
    }
  },
  beforeMount() {
    article()
      .then((re) => {this.article = re.data.posts})
      .catch((err) => console.log(err))
  },
}
</script>