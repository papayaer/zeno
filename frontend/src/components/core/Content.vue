<template>
  <v-card flat v-if="imgSrc && (imgSrc.length == 1)">
    <v-img v-for="(item, index) in imgSrc" :key="index" class="white--text align-end"
      :src="item"
      max-height="17rem"
      min-height="8rem">
      <slot>
        <v-card-actions v-if="post.title" v-text="post.title"></v-card-actions>
      </slot>
    </v-img>
    <v-card-text v-if="post.abstract" class="px-0 py-2" v-html="post.abstract"></v-card-text>
  </v-card>

  <v-card flat v-else-if="imgSrc && (imgSrc.length > 1)">
    <v-img v-for="(item, index) in imgSrc" :key="index"
      :src="item"
      width="5.5rem"
      aspect-ratio="1"
      class="d-inline-block"
      style="margin-left:0.141rem;margin-right:0.141rem"
    ></v-img>
  </v-card>
  
  <v-card flat v-else-if="videoSrc && videoSrc.length">
    <h3 class="px-0">分享了视频短片</h3>
    <v-card-text class="px-0 py-1 body-1">{{ videoSrc[0] }}</v-card-text>
  </v-card>

  <v-card flat v-else>
    <v-card-text v-if="post.abstract" class="px-0 py-1 body-1" v-text="post.abstract"></v-card-text>
  </v-card>
</template>

<script>
export default {
  props:{
    post: [Object,Array]
  },
  data() {
    return {
      imgSrc: [],
      videoSrc: []
    }
  },
  created() {
    this.imgReg()
    this.videoReg()
  },
  filters: {
    body: function (params) {
      return params.length > '140' ? params.slice(0,140)+' ....' : params
    }
  },
  methods: {
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
  }
}
</script>