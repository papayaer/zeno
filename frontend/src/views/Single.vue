<template>
  <v-row no-gutters justify="center">
    <v-col cols="12">
      <v-row>
        <v-col v-if="loading" cols="12" class="pb-2">
          <v-skeleton-loader
            transition="fade-transition"
            height="100%"
            type="article"
          ></v-skeleton-loader>
        </v-col>
        <v-col cols="12" class="pb-2" v-else>
          <v-card outlined class="v-card--shadow pa-3 pa-sm-8" v-if="article">
            <v-card-title v-if="article.title" class="pa-0">
              <h2>{{ article.title }}</h2>
            </v-card-title>

            <v-card flat class="my-4 caption grey--text">
              <v-list-item class="px-2 border-dotted">
                <v-list-item-avatar height="3.2rem" width="3.2rem" color="grey" class="my-0 ml-0 mr-2">
                  <v-img :src="article.author.avatar"></v-img>
                </v-list-item-avatar>
                <v-list-item-content class="py-0">
                  <v-list-item-title class="align-self-start subtitle-1 font-weight-bold">
                    <router-link v-text="article.author.nickname" :to="{ path: '/user/'+article.author.id+'/index' }"></router-link>
                    <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
                    <span class="caption grey--text">发布: 2019年11月15日</span>
                    <!-- <v-chip dark small color="secondary" class="caption">{{ article.author.bio }}</v-chip> -->
                  </v-list-item-title>
                  <v-list-item-subtitle class="caption grey--text">
                    <div class="d-inline-flex mr-4">关注<span class="ml-1">{{ article.author.followed_count }}</span></div>
                    <div class="d-inline-flex mr-4">粉丝<span class="ml-1">{{ article.author.follower_count }}</span></div>
                    <div class="d-inline-flex mr-4">文章<span class="ml-1">{{ article.author.post_count }}</span></div>
                    <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{ article.author.comment_count }}</span></div>
                    <div class="d-inline-flex mr-4">收藏<span class="ml-1">{{ article.author.favorite_count }}</span></div>
                  </v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <span class="grey--text">字数 {{ article.body_html.length }}</span>
                  <span class="grey--text">阅读 23.6K</span>
                </v-list-item-action>
              </v-list-item>
            </v-card> 
            
            <v-card flat class="markdown-body single-text" v-html="article.body_html"></v-card>

            <v-card-actions class="">
              <core-comment class="mr-4" :post="article.author"></core-comment>
              <core-favorite :post="article.author"></core-favorite>
              <div class="flex-grow-1"></div>
            </v-card-actions>
            <v-divider class=""></v-divider>

            <v-card-actions class="">
              <v-card-text class="text-center">
                <core-share><span class="body-1 px-md-4">分享</span></core-share>
              </v-card-text>
            </v-card-actions>

            <v-card flat  class="justify-center">
              <v-list-item class="px-2 border-dotted">
                <v-list-item-avatar color="grey" class="my-0 ml-0 mr-2">
                  <v-img :src="article.author.avatar"></v-img>
                </v-list-item-avatar>
                <v-list-item-content class="py-0">
                  <v-list-item-title class="align-self-start subtitle-1 font-weight-bold">
                    <router-link v-html="article.author.nickname" :to="{ path: '/user/'+article.author.id+'/index' }"></router-link>
                    <v-icon small class="mx-1" color="primary">mdi-check-decagram</v-icon>
                    <span class="caption grey--text">{{ article.author.bio }}</span>
                  </v-list-item-title>
                  <v-list-item-subtitle class="caption grey--text">
                    <div class="d-inline-flex mr-4">关注<span class="ml-1">{{ article.author.followed_count }}</span></div>
                    <div class="d-inline-flex mr-4">粉丝<span class="ml-1">{{ article.author.follower_count }}</span></div>
                    <div class="d-inline-flex mr-4">文章<span class="ml-1">{{ article.author.post_count }}</span></div>
                    <div class="d-inline-flex mr-4">讨论<span class="ml-1">{{ article.author.comment_count }}</span></div>
                    <div class="d-inline-flex mr-4">收藏<span class="ml-1">{{ article.author.favorite_count }}</span></div>
                  </v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <core-follow :user="article.author"></core-follow>
                </v-list-item-action>
              </v-list-item>
            </v-card>
          </v-card>
        </v-col>

        <v-col cols="12" class="py-1">
          <v-card outlined class="v-card--shadow">
            <v-card-text>
              <h3 class="pl-3" style="border-left:4px solid #fb3a59;">全部笔记</h3>
              <template v-for="(item, index) in comments">
                <core-comments :key="index" :item="item"></core-comments>
              </template>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col cols="12" class="py-2">
          <core-write :iscomment="true"></core-write>
        </v-col>

        <v-col cols="12" class="py-2">
          <v-card outlined class="v-card--shadow">
            <v-card-title>
              <strong class="pl-3 body-1" style="border-left:4px solid #fb3a59;">推荐阅读</strong>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-col>

    <!-- <v-col md="3" cols="12">
      <v-row>
        <v-col cols="12" v-if="article">
          <core-single-bar :item="article"></core-single-bar>
        </v-col>
      </v-row>
    </v-col> -->
  </v-row>
</template>

<script>
import { details, get_post_comments } from '@/api/posts'

export default {
  data() {
    return {
      article: null,
      comments: null,
      loading: true
    }
  },
  created() {
    this.post_details()
    this.get_comment()
  }, 
  methods: {
    post_details() {
      details(this.$route.params.postid)
        .then((re) => {
          this.loading = false
          this.article=re.data.post
          this.$store.dispatch('currentPost', this.article)
        })
    },
    get_comment() {
      get_post_comments(this.$route.params.postid)
      .then(re => { 
        this.comments = re.data.posts
      })
    },
    handleScroll() {
      let notdisp = document.getElementsByClassName('nav-bar')
      let isdisp = document.getElementsByClassName('bar-post-title')
      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
        if (scrollTop > 75) {
          notdisp[0].classList.add('not-display')
          isdisp[0].classList.add('is-display')
          // console.log(scrollTop)
        } else { // 恢复样式
          notdisp[0].classList.remove('not-display')
          isdisp[0].classList.remove('is-display')
        }
    }
  },
  beforeRouteLeave (to, from, next) {
    let notdisp = document.getElementsByClassName('nav-bar')
    let isdisp = document.getElementsByClassName('bar-post-title')
    notdisp[0].classList.remove('not-display')
    isdisp[0].classList.remove('is-display')
    next()
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll)
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>
