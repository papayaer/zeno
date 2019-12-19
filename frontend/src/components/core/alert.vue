<template>
  <v-alert v-model="alert" type="error">
      I'm an error alert.
  </v-alert>
</template>

<script>
export default {
  props: {
    alert: null
  }
}
</script>