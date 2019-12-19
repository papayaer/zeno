<template>
  <v-footer padless color="transparent">
    <v-col sm="5" cols="12" class="text-md-left px-0 caption">
      © {{ new Date().getFullYear() }}
      <span>蓝皮小虾</span>
      <router-link class="ml-3" to="/">首页</router-link>
      <router-link class="ml-3" to="/explore">浏览</router-link>
      <router-link class="ml-3" :to="{path: '/user/'+$route.params.author+'/writepost'}">笔记</router-link>
      <router-link class="ml-3" to="/activity">瀑布流</router-link>
      <router-link class="ml-3" to="/test">测试</router-link>
      <router-link class="ml-3" to="/about">关于</router-link>
    </v-col>

    <v-col sm="2" cols="2" class="text-center px-0">
      <v-btn text icon small color="gary">
        <v-icon>mdi-camera</v-icon>
      </v-btn>
    </v-col>
    
    <v-col sm="5" cols="10" class="text-sm-right px-0">
      <v-btn text icon small color="gary" class="mr-3"><v-icon>mdi-wechat</v-icon></v-btn>
      <v-btn text icon small color="gary" class="mr-3"><v-icon>mdi-qqchat</v-icon></v-btn>
      <v-btn text icon small color="gary" class="mr-3"><v-icon>mdi-linkedin</v-icon></v-btn>
      <v-btn text icon small color="gary"><v-icon >mdi-instagram</v-icon></v-btn>
    </v-col>
  </v-footer>
</template>