import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'


Vue.config.productionTip = false

Vue.directive('hasRole', {
  inserted(el, binding, vnode) {
    if (binding.value !== store.getters.getLoggedInUserRole) {
      vnode.elm.parentElement.removeChild(vnode.elm)
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')