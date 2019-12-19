<template>
  <v-card outlined class="v-card--shadow">
    <v-card-text v-if="!iscomment" class="pb-0">
      <v-textarea
        v-model="title"
        name="title"
        label="文章标题"
        prepend-icon="mdi-alphabetical"
        rows="1"
        auto-grow
        hide-details
      ></v-textarea>
    </v-card-text>

    <v-card-text v-if="!iscomment" class="pb-0">
      <v-textarea
        v-model="abstract"
        name="abstract"
        label="摘要/导语"
        prepend-icon="mdi-text"
        rows="1"
        auto-grow
        hide-details
      ></v-textarea>
    </v-card-text>

    <v-card-text class="d-flex align-start">
      <v-avatar v-if="iscomment" color="grey" size="36" class="d-none d-sm-flex mr-3">
        <img v-if="$store.state.isLogin" :src="$store.state.currentUser.avatar">
      </v-avatar>
      <div id="editor" style="width:100%;display:inline-grid;">
        <h3 v-if="$store.state.isLogin && iscomment" class="py-1">{{$store.state.currentUser.nickname}}</h3>
        <mavon-editor
          ref="editor"
          placeholder="笔记支持markdown"
          v-model="contnet"
          :subfield="false"
          :boxShadow="false"
          :toolbars="toolbars"
          codeStyle="atom-one-light"
          style="z-index:inherit;min-width:200px;min-height:200px;">
        </mavon-editor>
      </div>
    </v-card-text>

    <v-card-actions v-if="iscomment" class="px-4 pt-0">
      <div class="pl-12 body-2">
        <span>Ctrl + Enter 发表</span>
      </div>
      <div class="flex-grow-1"></div>
      <div>
        <v-btn :disabled="disabled" tile small color="primary"
          @click="doWrite">{{ save }}</v-btn>
        <!-- <v-btn outlined rounded small @click="comment = null" color="grey" class="ml-2">取消</v-btn> -->
      </div>
    </v-card-actions>

    <v-card-actions v-if="!iscomment" class="px-sm-4 caption grey--text">
      <span>#表情</span>
      <span class="ml-2">#图片</span>
      <span class="ml-2">#视频</span>
      <span class="ml-2">#话题</span>
      <span class="ml-2">#树洞</span>
      <div class="flex-grow-1"></div>
      <v-btn :disabled="disabled" tile small color="primary" @click="doPost">{{ save }}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { writeComment } from '@/api/comments'
import { writePost } from '@/api/posts'
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

export default {
  name: 'editor',
  components: {
    mavonEditor
  },
  props: {
    iscomment: {
      type: [Boolean,String],
      default: false
    }
  },
  data() {
    return {
      title: '',
      abstract: '',
      contnet: '',
      save: '分享笔记',
      disabled: false,
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: false, // 下划线
        strikethrough: true, // 中划线
        mark: false, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: false, // 无序列表
        link: false, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: false, // 表格
        fullscreen: false, // 全屏编辑
        readmodel: false, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: false, // 帮助
        /* 1.3.5 */
        undo: false, // 上一步
        redo: false, // 下一步
        trash: false, // 清空
        save: false, // 保存（触发events中的save事件）
        /* 1.4.2 */
        navigation: false, // 导航目录
        /* 2.1.8 */
        alignleft: false, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true, // 预览
      }
    }
  },
  methods: {
    doWrite() {
      this.save = '正在发布'
      this.disabled = true
      // $refs获取编译后的html. v-model只能获取源markdown
      let body_html = this.$refs.editor.d_render
      const postBody = { 
        body: body_html
       }
      if (this.$store.state.isLogin && (this.contnet.length >= 2)) {
        writeComment(this.$route.params.postid, postBody)
        .then(re => { 
          this.save = '发布'
          this.disabled = false
          this.contnet = ''
          console.log(re.data)
        })
      }
    },
    doPost() {
      this.save = '正在发布'
      this.disabled = true
      // $refs获取编译后的html. v-model只能获取源markdown
      let body_html = this.$refs.editor.d_render
      let title = this.title
      let abstract = this.abstract  //文章摘要
      const postBody = { 
        title: title,
        abstract: abstract,
        body: body_html
       }
      if (body_html.length > 2) {
        writePost(postBody)
        .then(re => { 
          this.save = '分享笔记'
          this.disabled = false
          console.log(re.data)
        })
      }
    }
  }
}
</script>