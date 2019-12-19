<template>
  <div v-if="imgarr.length == 1">
    <v-img v-for="(item, index) in imgarr" :key="index"
      :src="item"
      max-height="17rem"
      min-height="8rem">
      <v-row v-if="imginfo" no-gutters class="fill-height align-content-space-between">
        <v-col cols="12">
          <v-card-subtitle class="caption text-right">
            <v-chip dark small class="text-uppercase">视频</v-chip>
          </v-card-subtitle>
        </v-col>
        <v-col cols="12">
          <v-card-actions>
            <v-avatar size="1.6rem">
              <img :src="post.author.avatar">
            </v-avatar>
            <router-link class="mx-2 text-bgshadow white--text" v-text="post.author.nickname" :to="{ path: `/user/${post.author.id}/index` }"></router-link>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-img>
  </div>

  <div flat v-else-if="imgarr.length > 1">
    <v-img v-for="(item, index) in imgarr" :key="index"
      :src="item"
      :width="imgarr.length == 2 ? '48.333%' : '23.333%'"
      aspect-ratio="1"
      class="d-inline-block"
      style="margin-left:0.141rem;margin-right:0.141rem"
    ></v-img>
  </div>
  
  <div flat v-else-if="videoarr.length > 0">
    <v-card-text class="pa-0">
      {{ videoarr[0] }}
    </v-card-text>
  </div>
</template>

<script>
export default {
  props:{
    post: [Object,Array],
    imgarr: [Object,Array],
    videoarr: [Object,Array],
    imginfo: {
      type: Boolean,
      default: false
    },
    height: {
      type: String,
      default: '10rem'
    }
  }
}
</script>