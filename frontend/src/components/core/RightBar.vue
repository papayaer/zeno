<template>
<v-row>
  <v-col cols="12" class="pb-2">
    <v-card outlined class="v-card--shadow">
      <v-card-title class="pa-2 justify-space-between">
        <!-- <strong class="pl-3 title-1" style="border-left:4px solid #f5365c;">
          排行榜
        </strong> -->
        <v-tabs
          right
          show-arrows
          background-color="transparent">
        <v-tab v-for="item in items" :key="item" class="px-0">
          {{ item }}
        </v-tab>
      </v-tabs>
        <!-- <router-link class="caption grey--text right" to="">更多</router-link> -->
      </v-card-title>
      <v-card-text>
        <ul>
          <li v-for="(item, index) in 6" :key="index">{{item}}</li>
        </ul>
      </v-card-text>
    </v-card>
  </v-col>

  <v-col cols="12" class="py-2">
    <v-card outlined class="v-card--shadow">
      <v-img
        src="https://picsum.photos/300/200"
        height="116"
        max-height="116"
        :aspect-ratio="16/9">
        <v-card-title>要让荤食者也喜爱素食</v-card-title>
        <v-card-actions class="justify-end">Listen Now</v-card-actions>
      </v-img>
    </v-card>
  </v-col>

  <v-col cols="12" class="py-2">
    <v-card outlined class="v-card--shadow">
      <v-card-title class="pa-2 justify-space-between">
        <strong class="pl-3 title-1" style="border-left:4px solid #f5365c;">
          最新投稿的UP主
        </strong>
        <router-link class="caption grey--text right" to="">更多</router-link>
      </v-card-title>
      <v-card-text class="text-left justify-start">
        <v-avatar
          size="35"
          class="ma-1"
          v-for="(n, i) in 18" :key="i">
          <v-img :src="`https://randomuser.me/portraits/women/${n}.jpg`"></v-img>
        </v-avatar>
      </v-card-text>
    </v-card>
  </v-col>

</v-row>
</template>

<script>
export default {
  data() {
    return {
      items: ['昨天','前天','周榜','月榜']
    }
  },
}
</script>