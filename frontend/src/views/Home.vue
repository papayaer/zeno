<template>
  <v-content style="min-height: calc(100vh - 64px);padding-top: 0;">
    <core-banner style="height:50vh" :class="[$route.name == 'home'?'align-end':'align-center']">
      <v-container v-if="$route.name == 'explore'" class="container-xl">
        <v-row justify="center">
          <v-col sm="11" md="9" cols="12">
            <v-text-field dark
              label="搜索你想要的答案..."
              solo-inverted
              single-line
              hide-details
              prepend-inner-icon="mdi-magnify"
              class="mb-sm-5">
            </v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </core-banner>
    <v-divider></v-divider>
    <v-container class="container-xl">
      <!-- <v-row justify="center" class="mx-n7 mx-sm-0">
        <v-col sm="11" md="9" cols="12" class="pb-0">
          <v-breadcrumbs :items="items" class="pa-0">
            <template v-slot:divider>
              <v-icon>mdi-chevron-right</v-icon>
            </template>
          </v-breadcrumbs>
        </v-col>
      </v-row> -->

      <v-row justify="center" class="mx-sm-0">
        <v-col sm="11" md="9" cols="12">
          <v-fade-transition mode="out-in">
            <router-view></router-view>
          </v-fade-transition>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          text: '全部',
          disabled: false,
          href: '/',
        },
        {
          text: this.$route.name,
          disabled: false,
        },
      ]
    }
  },
}
</script>