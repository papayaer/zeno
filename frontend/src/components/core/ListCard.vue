<template>
  <v-card flat hover class="v-card--shadow pa-sm-3">
    <v-row no-gutters>
      <v-col sm="4" cols="12">
        <v-skeleton-loader v-if="!imgSrc.length"
          transition="fade-transition"
          boilerplate
          height="9em"
          type="image"
        ></v-skeleton-loader>
        <core-image v-else 
          :imgarr="imgSrc"
          :post="post"
        ></core-image>
      </v-col>

      <v-col sm="8" cols="12" class="d-flex align-content-space-between flex-wrap">
        <div style="width:100%">
          <v-card-subtitle class="py-1 pt-sm-0 caption grey--text">
            图片<span class="mx-1">·</span>视频
          </v-card-subtitle>
          <v-card-title v-if="post.title" class="body-2 font-weight-black py-1 py-sm-0">
            <router-link :to="{ path: `/post/${post.id}/single`}" v-text="post.title"></router-link>
          </v-card-title>
          <v-list-item-subtitle class="px-4 py-2" v-if="post.abstract" v-text="post.abstract"></v-list-item-subtitle>
        </div>

        <v-card-actions class="px-4 pb-sm-0 caption" style="width:100%">
          <v-avatar size="1.3rem" class="mr-1">
            <img :src="post.author.avatar">
          </v-avatar>
          <router-link class="grey--text" :to="{ path: `/user/${post.author.id}/index`}" v-text="post.author.nickname"></router-link>
          <div class="flex-grow-1"></div>
          <v-icon small class="mr-1">mdi-heart</v-icon>
          <span class="subheading">{{ post.comment_count }}</span>
          <span class="mx-2">·</span>
          <v-icon small class="mr-1">mdi-share-variant</v-icon>
          <span class="subheading">{{ post.favorite_count }}</span>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { format } from '@/utils'

export default {
  props:{
    post: [Object,Array]
  },
  data() {
    return {
      imgSrc: [],
      videoSrc: [],
      show: false,
      active: false,
      amenities: true,
      width: null,
      Viewport: null
    }
  },
  created() {
    this.imgReg()
    this.videoReg()
    // this.viewBreak()
  },
  filters: {
    format: function (params) {
      return format(params)
    },
    body: function (params) {
      return params.length > '80' ? params.slice(0,79)+' ....' : params
    }
  },
  methods: {
    viewBreak() {
      window.innerWidth < 600 ? this.Viewport = true : this.Viewport = false
      return this.width = window.innerWidth
    },
    imgReg() {
      const content = this.post.body_html
      const reg = /<img.*?\bsrc\b\s*=\s*".*?(?:\s*">|\s*"\/>)/gi
      if (reg.test(content)) {//test() 方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false
        let img = content.match(reg)
        img.forEach(str => {
          if (str.length) {
            let srcstr = str.match(/\bsrc\b\s*=\s*"/gi).toString().length
            let start = str.search(/\bsrc\b\s*=\s*"/gi)+srcstr
            let last = str.search(/(?:\s*">|\s*"\/>)/g)
            let src = str.slice(start,last)
            this.imgSrc.push(src)
          }
        });
      }
    },
    videoReg() {
      const content = this.post.body_html
      const reg = /(?:<video|<source).*?\bsrc\b\s*=\s*".*?(?:\s*">|\s*"\/>|"\s*\/>)/gi
      if (reg.test(content)) {
        let video = content.match(reg)
        video.forEach(str => {
          if (str.length) {
            let srcstr = str.match(/\bsrc\b\s*=\s*"/gi).toString().length
            let start = str.search(/\bsrc\b\s*=\s*"/gi)+srcstr
            let last = str.search(/(?:\s*">|\s*"\/>|"\s*\/>)/g)
            let src = str.slice(start,last)
            this.videoSrc.push(src)
          }
        })
      }
    }
  },
  mounted() {
    window.addEventListener("resize", this.viewBreak)
  },
}
</script>

