<template>
  <v-row justify="center">
    <template v-if="!article.length">
      <v-col v-for="(item, index) in 3" :key="index" cols="12" class="pa-2">
        <transition name="fade" mode="in-out">
          <v-card flat class="v-card--shadow pa-sm-3">
            <v-row no-gutters>
              <v-col sm="4" cols="12">
                <v-skeleton-loader
                  transition="fade-transition"
                  height="9em"
                  type="image"
                ></v-skeleton-loader>
              </v-col>
              <v-col sm="8" cols="12" class="d-flex align-content-space-between flex-wrap">
                <div style="width:100%">
                  <v-skeleton-loader
                    transition="fade-transition"
                    type="article"
                  ></v-skeleton-loader>
                </div>
              </v-col>
            </v-row>
          </v-card>
      </transition>
      </v-col>
    </template>
    
    <template v-else>
      <v-col cols="12" class="pa-2" v-for="(item, index) in article" :key="index">
        <transition name="fade" mode="out-in">
          <core-list-card
            :post="item"
            :downtitle="true">
          </core-list-card>
        </transition>
      </v-col>
    </template>

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
import { article } from '@/api/posts'

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
  computed: {
    itemWidth(){
      return (138*0.5*(document.documentElement.clientWidth/375))  //rem to layout, Calculate the value of width 
    },
    gutterWidth(){
      return (9*0.5*(document.documentElement.clientWidth/375)) //rem to layout, Calculate the value of margin 
    }
  },
  methods: {
    async fetchPost() {
      this.loading = true
      await article(this.page)
        .then(re => {
          this.loading = false
          re.data.next ? this.page ++ : this.loadmsg = '没有了'
          this.article = this.article.concat(re.data.posts)
        })
    }
  }
}

</script>