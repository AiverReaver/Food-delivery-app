import Vue from 'vue'
import SuiVue from 'semantic-ui-vue';

import App from './App.vue'
import router from './router'
import store from './store'


Vue.config.productionTip = false
Vue.use(SuiVue)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')