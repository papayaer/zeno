<template>
<v-row>
  <v-col md="12" sm="2" cols="4" class="pb-md-0">
    <v-card flat color="transparent" class="mx-auto">
      <v-img
        :src="user.avatar"
        aspect-ratio="1"
      ></v-img>
      <v-card-title v-if="user.about_me" class="d-none d-sm-none d-md-flex pa-0 pt-1">
        <span class="caption px-1">💕 {{user.about_me}} 🌊</span>
      </v-card-title>
    </v-card>
  </v-col>

  <v-col md="12" sm="6" cols="8">
    <v-card flat color="transparent">
      <v-list-item-title class="pt-md-1 title">
        {{user.username}}
        <v-icon small color="primary">mdi-check-decagram</v-icon>
      </v-list-item-title>
      <v-list-item-subtitle class="grey--text">{{user.nickname}}</v-list-item-subtitle>

      <v-card-text class="d-flex d-md-none pa-0 py-sm-2">
        <span fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</span>
        <span class="caption px-1">{{user.about_me}}</span>
      </v-card-text>

      <v-card-actions class="px-0 pb-0">
        <v-btn v-if="$store.state.currentUser.id == $route.params.author"
          depressed block dark color="primary" :to="{path: '/user/'+currentUser.id+'/profile'}">
          我的资料
        </v-btn>
        <core-follow v-else :user="user" class="v-btn--block"></core-follow>
      </v-card-actions>
    </v-card>
  </v-col>

  <v-col cols="12" class="d-none d-md-flex">
    <v-card flat color="transparent" class="flex-grow-1">
      <v-card-actions class="caption pa-0">
        <v-icon small class="mr-1">mdi-map-marker-outline</v-icon>{{user.location}}
      </v-card-actions>
      <v-card-actions class="caption pa-0">
        <v-icon small class="mr-1">mdi-link</v-icon>{{user.website_url}}
      </v-card-actions>
    </v-card>
  </v-col>

  <v-col cols="12" class="d-none d-md-flex">
    <v-card flat color="transparent" class="flex-grow-1">
      <v-divider class="mb-3"></v-divider>
      <v-card-actions class="caption px-0">
        <v-icon size="18" class="mr-1">mdi-instagram</v-icon>
        <v-icon size="18" class="mr-1">mdi-linkedin</v-icon>
        <v-icon size="18" class="mr-1">mdi-qqchat</v-icon>
        <v-icon size="18" class="mr-1">mdi-wechat</v-icon>
      </v-card-actions>
      <v-card-actions class="pl-0 caption">
        <v-icon small class="mr-1">mdi-calendar-range-outline</v-icon>
        last:{{user.last_seen}}
      </v-card-actions>
    </v-card>
  </v-col>

</v-row>
</template>

<script>
import { mapState } from 'vuex'
import { author } from '@/api/users'

export default {
  computed: {
    ...mapState([
      'currentUser'
    ])
  },
  data() {
    return {
      user: {},
      editText: '',
      editProfile: null
    }
  },
  created() {
    this.getAuthor()
  },
  watch: {
    '$route':'getAuthor'
  },
  methods: {
    getAuthor() {
      if (this.$route.params.author && this.currentUser.id) {
        this.editText = '个人资料'
        this.editProfile = `{path: /user/${this.currentUser.id}/profile}`
      }
      return author(this.$route.params.author)
            .then((response) => this.user = response.data)
    }
  },
}
</script>