<template>
  <v-card flat class="mt-5 pt-5">
    <v-sheet dark color="primary" class="elevation-card mt-n10 mx-4 pa-3" style="border-radius:4px;">
      <h4 class="title font-weight-light mb-1">个人资料</h4>
      <span class="caption category font-weight-thin">完善您的个人资料</span>
    </v-sheet>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="4">
          <v-file-input show-size accept="image/png, image/jpeg, image/bmp"
            :rules="avatarules" :placeholder="avatar" prepend-icon="mdi-camera"
          ></v-file-input>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field v-model="nickname" label="nickname"
            :hint="nicknamehint" type="text"></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <!-- <v-autocomplete
            :items="sex" label="性别" multiple
          ></v-autocomplete> -->
        </v-col>
        <v-col cols="12">
          <v-text-field v-model="bio" label="bio"
            :hint="biohint" type="text"></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field v-model="email" label="Email*"
            :hint="emailhint" type="text" required></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field v-model="password" label="Password*"
            :append-icon="show1 ? 'mdi-visibility' : 'mdi-visibility_off'"
            :type="show ? 'text' : 'password'"
            :hint="passwordhint" persistent-hint required></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions class="justify-end">
      <v-btn depressed dark
        :loading="loading"
        :disabled="disabled"
        color="primary" @click="updateProfile"
      >{{btntext}}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { up_user } from '@/api/authentication'

export default {
  data() {
    return {
      btntext: '确认',
      show: null,
      show1: false,
      loading: false,
      disabled: false,
      bio: this.$store.state.currentUser.bio,
      biohint: '你的状态',
      nickname: this.$store.state.currentUser.nickname,
      nicknamehint: '用于公开的昵称',
      email: this.$store.state.currentUser.email,
      emailhint: '用于登录或订阅信息',
      password: null,
      passwordhint: '确保至少15个字符或至少8个字符（ 包括数字 和小写字母 ）。',
      sex: ['男', '女', '保密'],
      sexhint: '',
      avatar: '头像url',
      avatarules: /w.*/,
    }
  },
  methods: {
    updateProfile(){
      if (this.$store.getters.isAuthenticated) {//检查登录否?
        let userData = { 'nickname': this.nickname }
        let author = this.$store.state.currentUser.id
        return up_user(author, userData)
                .then(() => { this.$store.dispatch('ref', author) })
      }
      // console.log(u_id,this.nickname)
    }
  },
}
</script>