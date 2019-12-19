<template>
  <div class="caption d-flex align-center">
    <v-btn small icon @click="show = !show">
      <svg t="1565185677559" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="651" width="18" height="18"><path d="M536.32 768H608a288 288 0 0 0 0-576h-192a288 288 0 0 0-56.32 570.24L384 768v119.04z m-142.72 192A44.8 44.8 0 0 1 320 926.08V819.2A352 352 0 0 1 416 128h192a352 352 0 0 1 0 704h-49.28z" fill="grey" p-id="652"></path></svg>
    </v-btn>
    <slot></slot>
    {{ post.comment_count }}
  </div>
</template>

<script>

export default {
  props: {
    post: {
      type: [Object, Array],
      default: null
    }
  },
  data() {
    return {
      show: false 
    }
  }
}
</script>