<template>
  <v-content>
    <v-container class="container-xl">
      <v-row>
        <v-col id="col-one" md="3" cols="6" class="px-1 px-md-3">
          <v-card class="elevation-card mb-2 mb-md-6" v-for="(item, index) in one" :key="index">
            <v-img
              class="white--text"
              gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
              height="400px"
              :src="`/assets/img/${item}-900x325.jpg`">
              <v-row no-gutters>
                <v-col cols="12" class="pa-2 text-right">
                  <v-chip
                    label
                    class="text-uppercase"
                    color="grey darken-3"
                    text-color="white"
                    small>
                    类别
                  </v-chip>
                </v-col>
              </v-row>
            </v-img>
            <v-card-title class="title font-weight-light">昵称{{ item }}注册</v-card-title>
            <v-card-text class="subheading font-weight-light grey--text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus.</v-card-text>
            <v-divider></v-divider>
            <v-card-actions class="grey--text font-weight-light">
              <v-avatar size="22" class="mr-1">
                <v-img :src="`https://randomuser.me/portraits/women/${item}.jpg`"></v-img>
              </v-avatar>
              <span class="caption">username{{ item }}</span>
              <div class="flex-grow-1"></div>
              <v-btn icon small><v-icon size='18'>mdi-heart-outline</v-icon></v-btn>
              <span class="caption mx-1">1</span>
            </v-card-actions>
          </v-card>
        </v-col>

        <v-col id="col-two" md="3" cols="6" class="px-1 px-md-3">
          <v-card class="elevation-card mb-2 mb-md-6" v-for="(item, index) in two" :key="index">
            <v-img
              class="white--text align-end"
              gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
              height="400px"
              :src="`/assets/img/${item}-900x325.jpg`">
              <v-card-title class="title font-weight-light">{{ item }} years ago in Lifestyle</v-card-title>
            </v-img>
            <v-card-text class="subheading font-weight-light grey--text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus.</v-card-text>
            <v-divider></v-divider>
            <v-card-actions class="grey--text font-weight-light">
              <v-avatar size="22" class="mr-1">
                <v-img :src="`https://randomuser.me/portraits/women/${item}.jpg`"></v-img>
              </v-avatar>
              <span class="caption">username{{ item }}</span>
              <div class="flex-grow-1"></div>
              <v-btn icon small><v-icon size='18'>mdi-heart-outline</v-icon></v-btn>
              <span class="caption mx-1">1</span>
            </v-card-actions>
          </v-card>
        </v-col>

        <v-col id="col-three" md="3" cols="6" class="px-1 px-md-3">
          <v-card class="elevation-card mb-2 mb-md-6" v-for="(item, index) in three" :key="index">
            <v-img
              class="white--text"
              gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
              height="400"
              :src="`/assets/img/${item}-900x325.jpg`">
              <v-row no-gutters>
                <v-col cols="12" class="pa-2 text-right">
                  <v-chip
                    label
                    class="text-uppercase"
                    color="grey darken-3"
                    text-color="white"
                    small>
                    类别
                  </v-chip>
                </v-col>
              </v-row>
            </v-img>
            <v-card-title class="title font-weight-light">昵称{{ item }}注册</v-card-title>
            <v-card-text class="subheading font-weight-light grey--text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus.</v-card-text>
            <v-divider></v-divider>
            <v-card-actions class="grey--text font-weight-light">
              <v-avatar size="22" class="mr-1">
                <v-img :src="`https://randomuser.me/portraits/women/${item}.jpg`"></v-img>
              </v-avatar>
              <span class="caption">username{{ item }}</span>
              <div class="flex-grow-1"></div>
              <v-btn icon small><v-icon size='18'>mdi-heart-outline</v-icon></v-btn>
              <span class="caption mx-1">1</span>
            </v-card-actions>
          </v-card>
        </v-col>

        <v-col id="col-four" md="3" cols="6" class="px-1 px-md-3">
          <v-card class="elevation-card mb-2 mb-md-6" v-for="(item, index) in four" :key="index">
            <v-img
              class="white--text align-end"
              gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
              height="400"
              :src="`/assets/img/${item}-900x325.jpg`">
              <v-card-title class="title font-weight-light">{{ item }} years ago in Lifestyle</v-card-title>
            </v-img>
            <v-card-text class="subheading font-weight-light grey--text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus.</v-card-text>
            <v-divider></v-divider>
            <v-card-actions class="grey--text font-weight-light">
              <v-avatar size="22" class="mr-1">
                <v-img :src="`https://randomuser.me/portraits/women/${item}.jpg`"></v-img>
              </v-avatar>
              <span class="caption">username{{ item }}</span>
              <div class="flex-grow-1"></div>
              <v-btn icon small><v-icon size='18'>mdi-heart-outline</v-icon></v-btn>
              <span class="caption mx-1">1</span>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  data() {
    return {
      all: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
      one: [1, 3], //#col-one的value
      two: [2, 4],  //#col-two的value
      three: [5, 6], //#col-tree的value
      four: [7, 8]  //#col-four的value
    }
  },
  methods: {
    readMore() {
      let c = this.all.length//文章总数
      let t = this.one.length+this.two.length+this.three.length+this.four.length //已经分配的
      let one = this.colHeight('col-one')//#col-one 高
      let two = this.colHeight('col-two')//#col-two 高
      let three = this.colHeight('col-three')//#col-three 高
      let four = this.colHeight('col-four')//#col-four 高
      let tabId = Math.min(one, two, three, four)//最小列
      
      if (t < c) {// 如果未分配完
        if (tabId == one) {
          this.one.push(this.all[t])
        } else if (tabId == two) {
          this.two.push(this.all[t])
        } else if (tabId == three) {
          this.three.push(this.all[t])
        } else if (tabId == four) {
          this.four.push(this.all[t])
        }
      }
    },
    colHeight(tabId) {//tabId 的高
      let tempHeight = 0
      let col = document.getElementById(tabId)
      let card = col.getElementsByClassName('v-card')
      for (let index = 0; index < card.length; index++) {
        const h = card[index].offsetHeight
        tempHeight += h
      }
      return tempHeight
    },
    handleScroll() {
      //视图更新后再执行
      this.$nextTick(() => {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
        if (scrollTop + window.innerHeight >= document.body.clientHeight) {
          this.readMore()
        }
      })
    },
    throttle(fn, delay) {//限频，每delay的时间执行一次
      let timer = null
      return () => {
        if (timer != null) clearTimeout(timer)
        timer = setTimeout(fn, delay)
      }
    },
  },
  mounted() {
    this.throttleLoad = this.throttle(() =>{ this.handleScroll() },300)
    // window.addEventListener("resize", this.viewBreak)
    window.addEventListener("scroll", this.throttleLoad)
  },
  destroyed() {
    window.removeEventListener('scroll', this.throttleLoad)
  },
}
</script>