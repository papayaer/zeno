<template>
  <v-row justify="center">
    <v-col cols="12">
      <v-tabs
        v-model="tab"
        show-arrows
        background-color="transparent">
        <v-tab
          v-for="item in items"
          :key="item">
          {{ item }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab" class="transparent pt-4">
        <v-tab-item
          v-for="(item,i) in items"
          :key="item">
          <component v-bind:is="currentTab[i]"></component>
        </v-tab-item>
      </v-tabs-items>
    </v-col>
  </v-row>
</template>

<script>

export default {
  components: {
    project: () => import('@/views/Project'),
    aboutme: () => import('@/views/About'),
    register: () => import('@/views/Register'),
    activity: () => import('@/views/Activity')
  },
  data() {
    return {
      article: [],
      tab: null,
      items: [
        '项目', '关于', '工作', '联系方式',
      ],
      currentTab: ['project','aboutme','register','activity'],
    }
  }
}
</script>