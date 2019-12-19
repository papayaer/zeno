import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import zhHans from 'vuetify/es5/locale/zh-Hans';

Vue.use(Vuetify);

const opts = {
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: '#f5365c', // #fb3a59,rgba(251, 9, 48, 0.8)
        secondary: '#f4f5f7',
        tertiary: '#495057',
        accent: '#82B1FF',
        error: '#f5365c',
        info: '#11cdef',
        success: '#2dce89',
        warning: '#fb6340',
        // anchor: '#000' // #ed1e24
      },
    },
  },
  lang: {
    locales: { zhHans },
    current: 'zh-Hans',
  },
};


export default new Vuetify(opts);