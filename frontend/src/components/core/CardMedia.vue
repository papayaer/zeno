<template>
  <v-card flat outlined class="v-card--shadow">
    <h3 class="text-center" style="height:16px;">
      <v-chip small color="primary" class="mt-n8">
        {{ post.timestamp | format }}
        <slot name="by"></slot>
      </v-chip>
    </h3>
    <v-card-subtitle :class="{ 'py-0': post.title }" v-if="tags">
      <v-chip x-small dark color="primary">类别</v-chip>
      标签1 / 标签2, Top Stories
    </v-card-subtitle>
    <v-card-title v-if="post.title && uptitle" class="pt-0 font-weight-bold">
      <router-link :to="{ path: `/post/${post.id}/single`}" v-text="post.title" ></router-link>
    </v-card-title>
    <v-card-text class="pt-0 pb-1" v-if="imgSrc.length > 0">
      <core-image :imgarr="imgSrc" :imginfo="imginfo" :post="post"></core-image>
    </v-card-text>
    <v-card-text class="pt-0 pb-1" v-if="videoSrc.length > 0">
      <core-image :videoarr="videoSrc"></core-image>
    </v-card-text>
    <v-card-title v-if="post.title && downtitle" class="pt-0 pb-1 font-weight-bold">
      <router-link :to="{ path: `/post/${post.id}/single`}" v-text="post.title" ></router-link>
    </v-card-title>
    <v-card-text v-if="post.abstract">
      {{ post.abstract | body }}
    </v-card-text>
    <v-card-subtitle class="pt-0" v-if="bytime">
      <v-chip x-small>
        发布 {{ post.timestamp | format }}
        | {{ post.timestamp }}
      </v-chip>
    </v-card-subtitle>
    <v-card-actions class="px-4 caption grey--text">
      <v-avatar size="1.6rem">
        <img :src="post.author.avatar">
      </v-avatar>
      <router-link class="mx-2" v-text="post.author.nickname" :to="{ path: `/user/${post.author.id}/index` }"></router-link>
      <div class="flex-grow-1"></div>
      <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{ post.comment_count }}</span></div>
      <div class="d-inline-flex">收藏<span class="ml-1">{{ post.favorite_count }}</span></div>
    </v-card-actions>
  </v-card>
</template>

<script>
import { format } from '@/utils'

export default {
  props:{
    post: [Object,Array],
    tags: {
      type: Boolean,
      default: false
    },
    uptitle: {
      type: Boolean,
      default: false
    },
    downtitle: {
      type: Boolean,
      default: false
    },
    imginfo: {
      type: Boolean,
      default: false
    },
    bytime: {
      type: Boolean,
      default: false
    }
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

