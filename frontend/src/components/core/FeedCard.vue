<template>
  <v-card flat tile
    v-bind="$attrs"
    color="grey lighten-1"
    dark>
    <v-img
      :src="`/assets/articles/${img}`"
      height="100%"
      gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)">
      <v-row no-gutters class="fill-height align-content-space-between">
        <v-col cols="12">
          <v-card-subtitle class="caption text-right">
            <v-chip dark small class="text-uppercase" @click.stop="">视频</v-chip>
            <h3 class="title text-bgshadow white--text font-weight-bold mb-2">
              {{ value.title }}
            </h3>
            <div class="caption white--text">
              {{ value.author.nickname }}<br>{{ value.timestamp}}
            </div>
          </v-card-subtitle>
        </v-col>
        <v-col cols="12">
          <v-card-subtitle class="text-right">
            <v-chip dark small class="text-uppercase" color="primary" :to="{ path: `/post/${value.id}/single`}">readme</v-chip>
          </v-card-subtitle>
        </v-col>
      </v-row>
    </v-img>
  </v-card>
</template>

<script>
export default {
  props: {
    value: [Object],
    img: [String]
  }
}
</script>