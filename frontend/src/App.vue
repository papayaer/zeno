<template>
  <v-app>
    <core-toolbar></core-toolbar>
    <core-main-view></core-main-view>
    <v-container class="container-xl pb-0">
      <v-row no-gutters justify="center">
        <v-col cols="12">
          <v-divider></v-divider>
          <core-main-footer></core-main-footer>
        </v-col>
      </v-row>
    </v-container>
    <core-dialogs></core-dialogs>
    <core-fab></core-fab>
  </v-app>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      // 
    }
  },
};
</script>

