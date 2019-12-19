<template>
  <v-card-actions class="px-4">
    <v-avatar size="22" color="grey" class="mr-2">
      <v-img :src="post.author.avatar"></v-img>
    </v-avatar>
    <span class="text-truncate">{{ post.author.nickname }}</span>

    <div class="flex-grow-1"></div>  
    <core-btn-comment :post="post" class="mr-2"></core-btn-comment>
    <core-btn-favorite :post="post"></core-btn-favorite>
  </v-card-actions>
</template>

<script>
export default {
  props:{
    post: [Object,Array]
  },
  data() {
    return {
      favorite: false
    }
  },
}
</script>