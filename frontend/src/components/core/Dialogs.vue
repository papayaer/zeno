<template>
  <v-dialog v-model="$store.state.dialog" max-width="500">
    <slot>
      <v-card>
        <v-card-title class="headline text-uppercase primary white--text">
          登录到papayaer
        </v-card-title>

        <v-card-text class="mt-4">
          <v-form>
            <v-text-field v-model="email"
              label="email / 用户名"
              name="login"
              prepend-icon="mdi-account-circle"
              type="text"
            ></v-text-field>

            <v-text-field v-model="password"
              id="password"
              label="密码"
              name="password"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn depressed block
            :loading="loading"
            :disabled="disabled"
            color="primary" @click="authenticate">{{text}}</v-btn>
        </v-card-actions>
      </v-card>
    </slot>

  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      errormsg: '',
      loading: false,
      disabled: false,
      text: '登录',
      email: 'Administrator@papayaer.me',
      password: 'hello'
    }
  },
  methods: {
    authenticate () {
      this.disabled = true
      this.loading = true
      this.$store.dispatch('login', { email: this.email, password: this.password })
        .then((re) => {
          this.disabled=false
          this.loading=false
          if (this.$store.getters.isAuthenticated) {//是否登录成功
            const to = `/user/${this.$store.state.currentUser.id}/index`
            const from = this.$route.fullPath
            if (to != from && this.$store.state.currentUser.id) {
              return this.$router.push({ path: to })
            }
          } else {//前端的验证失败后
            this.disabled = true
            this.loading=false
            this.text = '请更正错误信息后再次登录'
            setTimeout(() => {
              this.disabled=false
              this.text = '登录'},2000)
          }
        })
        .catch((Error) => {//后端验证失败后
          this.disabled = true
          this.loading=false
          this.text = Error
          setTimeout(() => {
            this.disabled=false
            this.text = '登录'},2000)
        })
    }

  }
}
</script>