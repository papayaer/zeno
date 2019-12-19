<template>
  <v-content>
    <v-container class="container-xl">
      <v-row justify="center">
        <v-col lg="11" md="10" cols="12">
          <core-write></core-write>
          <!-- <v-card-text class="pb-0">
            <v-file-input
              :rules="rules"
              accept="image/png, image/jpeg, image/bmp"
              placeholder="点击添加封面图"
              prepend-icon="mdi-camera"
            ></v-file-input>
          </v-card-text> -->
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>

export default {
  data() {
    return {
      title: '',
      abstract: '',
      contnet: '',
      save: '保存',
      disabled: false,
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: false, // 全屏编辑
        readmodel: false, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: false, // 帮助
        /* 1.3.5 */
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        save: false, // 保存（触发events中的save事件）
        /* 1.4.2 */
        navigation: false, // 导航目录
        /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true, // 预览
      }
    }
  }
}
</script>
