<template>
  <v-content style="min-height: calc(100vh - 64px);padding:0;">
    <core-banner style="height:50vh" class="align-end">
      <v-row no-gutters class="white">
        <v-col cols="12">
          <v-container class="container-xl py-0">
            <v-row no-gutters>
              <v-col lg="7" md="7" cols="12" offset-md="3" class="pl-md-1">
                <navtab></navtab>
              </v-col>
              <v-col lg="2" md="2" cols="12" class="d-none d-md-flex">
                <v-btn small rounded depressed dark class="align-self-center" color="primary" :to="{path: '/user/'+$route.params.author+'/profile'}">
                  获取电子邮件更新
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </core-banner>
    <v-divider></v-divider>
    <v-container class="container-xl">
      <v-row justify="center" class="mx-n8 mx-sm-0">
        <v-col lg="3" md="3" cols="12" class="py-0 pr-md-10">
          <core-user-bar style="margin-top:-210px"></core-user-bar>
        </v-col>
        <v-col lg="6" md="6" sm="8" cols="12" class="py-0">
          <v-fade-transition mode="out-in">
            <router-view></router-view>
          </v-fade-transition>
        </v-col>
        <v-col lg="3" md="3" sm="4" cols="12" class="pt-sm-4 pl-md-10">
          <core-right-bar class="pt-3"></core-right-bar>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  components: {
    Navtab: () => import('@/components/tab/Nav')
  }
}
</script>
