<template>
  <v-card flat>
    <v-img
      src="https://picsum.photos/400/220"
      gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
    ></v-img>
    <!-- <v-card-text v-if="article.abstract" v-html="article.abstract" class="py-0"></v-card-text> -->
  </v-card>
</template>

<script>
export default {
  props:{
    post: [Object,Array]
  }
}
</script>

