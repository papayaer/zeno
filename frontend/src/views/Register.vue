<template>
  <v-content>
    <v-container class="fill-height container-xl">
      <v-row justify="center">
        <v-col lg="5" md="5" cols="12">
          <div class="my-4 my-md-8 text-center">
            <span class="caption">加入木瓜派派</span>
            <h1 class="mt-3 mt-md-6">创建您的帐户</h1>
          </div>
          <v-form v-model="valid" class="py-4 py-md-8 ">
            <v-text-field class="my-3"
              v-model="email" :rules="emailRules"
              label="email / 用户名" name="login" type="text"
              prepend-icon="mdi-account-circle"
              :hint="emailhint"
            ></v-text-field>

            <v-text-field class="my-3"
              v-model="password" :rules="pwRules"
              id="password" label="密码" name="password"
              type="password" prepend-icon="mdi-lock"
              :hint="pwhint"
            ></v-text-field>
          </v-form>
          <v-btn depressed block
            :loading="loading"
            :disabled="disabled"
            color="primary" @click="register">{{text}}</v-btn>
          
          <div class="my-3 caption grey--text">
            创建帐户，即表示您同意<router-link class="ml-1" to="/site/terms">服务条款</router-link>。
            有关PapayaER隐私惯例的更多信息，请参阅<router-link class="ml-1" to="/site/privacy">PapayaER隐私声明</router-link>。
            我们有时会向您发送与帐户相关的电子邮件。
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import { fromValid } from '@/utils'

export default {
  components: {
    TabProfile: () => import('@/components/tab/Profile')
  },
  data() {
    return {
      valid: false,
      text: '注册',
      loading: false,
      disabled: false,
      email: '',
      emailRules: [
        v => !!v || 'E-mail是必填',
        v => /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/.test(v) || '请输入正确的E-mail地址',
      ],
      emailhint: '用户名只能包含字母数字字符或单个连字符，而不能以连字符开头或结尾。',
      password: '',
      pwRules: [
        v => !!v || '密码必填',
        v => /^.*(?=.{8,15})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#\$%\^&\*\?\(\),\.;:'"<>\{\}\[\]\\/\+-=\|_]).*$/.test(v) || '确保至少8个字符（ 包括数字 和小写字母 ）。',
      ],
      pwhint: '确保至少8个字符（ 包括数字 和小写字母 ）。',
    }
  },
  methods: {
    register() {
      this.disabled = true
      this.loading = true
      if (fromValid(this.email,this.password)) {
        this.$store.dispatch('doRegister', { email: this.email, password: this.password })
          .then((r) => {
            this.disabled=false
            this.loading=false
            this.text = '注册成功,正在登录...'
            if (this.$store.getters.isAuthenticated) {//是否登录成功
              const to = `/user/${this.$store.state.currentUser.id}/profile`
              return this.$router.push({ path: to })
            }
            console.log(r)
          })
          .catch((er)=> {
            this.loading=false
            this.text = '请更正错误信息后再次提交注册'
            setTimeout(() => {
              this.disabled=false
              this.text = '注册'},2000)})
      } else {
        this.loading=false
        this.text = '请更正错误信息后再次提交注册'
        setTimeout(() => {
          this.disabled=false
          this.text = '注册'},2000)
      }
      
    }
  }
}
</script>