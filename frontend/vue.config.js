const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')

module.exports = {
  lintOnSave: false,
  productionSourceMap:false,
  transpileDependencies: [ // Edge support
    'vuetify',
  ],
  configureWebpack: {
    plugins: [
      new VuetifyLoaderPlugin({
        /**
         * This function will be called for every tag used in each vue component
         * It should return an array, the first element will be inserted into the
         * components array, the second should be a corresponding import
         *
         * originalTag - the tag as it was originally used in the template
         * kebabTag    - the tag normalised to kebab-case
         * camelTag    - the tag normalised to PascalCase
         * path        - a relative path to the current .vue file
         * component   - a parsed representation of the current component
         */
        match (originalTag, { kebabTag, camelTag, path, component }) {
          if (kebabTag.startsWith('core-')) {
            return [camelTag, `import ${camelTag} from '@/components/core/${camelTag.substring(4)}.vue'`]
          }
        }
      })
    ]
  },
  css: {
    loaderOptions: {
      sass: {
        // @/ 是 src/ 的别名
        // 所以这里假设你有 `src/variables.sass` 这个文件
        // 注意：在 sass-loader v7 中，这个选项名是 "data"
        prependData: `@import "~@/styles/main.scss"`
      },
      scss: {
        // `scss` 语法会要求语句结尾必须有分号，`sass` 则要求必须没有分号
        // 在这种情况下，我们可以使用 `scss` 选项，对 `scss` 语法进行单独配置
        prependData: `@import "~@/styles/main.scss";`
      }
    },
  },
};