<template>
  <v-btn v-if="isfollow" text small dark color="primary" @click="unfollow">已关注</v-btn>
  <v-btn v-else small outlined rounded dark color="primary" @click="follow">+关注</v-btn>
</template>

<script>
import { doFollow, doUnFollow, hasFollow} from '@/api/follows'

export default {
  props: {
    user: {
      type: [Object, Array],
      default: null
    }
  },
  data() {
    return {
      isfollow: null
    }
  },
  created() {
    this.following()
  },
  watch: {
    'user':'following'
  },
  methods: {
    following() {// 关注了吗?
      if (this.$store.state.isLogin) {
        hasFollow(this.user.id)
          .then((re) => {
            re.data ? this.isfollow = true : this.isfollow = null
          })
          .catch((error) => console.log(error))
      }
    },
    follow() { //加关注
      if (this.$store.state.isLogin) {//查检是否登录
        doFollow(this.user.id)
          .then(() => this.following())
          .catch((error) => console.log(error))
      } else {
        console.log('请先登录')
      }
    },
    unfollow() {//取消关注
      if (this.$store.state.isLogin) {//查检是否登录
        doUnFollow(this.user.id)
          .then(() => this.following())
          .catch((error) => console.log(error))
      }
    }
  }
}
</script>