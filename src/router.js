import Vue from 'vue'
import Router from 'vue-router'
import Restaurants from './views/Restaurants.vue'
import store from './store';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/',
      name: 'home',
      component: Restaurants
    },
    {
      path: '/restaurants/:id',
      name: 'restaurant-detail',
      component: () => import( /* webpackChunkName: "restaurants-detail" */ './views/RestaurantDetail.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import( /* webpackChunkName: "login" */ './views/Login.vue'),
      beforeEnter: (to, from, next) => {

        if (store.getters.isLoggedIn)
          next('/')
        else
          next()
      }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import( /* webpackChunkName: "register" */ './views/Register.vue'),
      beforeEnter: (to, from, next) => {

        if (store.getters.isLoggedIn)
          next('/')
        else
          next()
      }
    },
    {
      path: '/create',
      name: 'create',
      component: () => import( /* webpackChunkName: "create" */ './views/RestaurantCreate.vue'),
      beforeEnter: (to, from, next) => {

        if (store.getters.getLoggedInUserRole === 'restaurant')
          next()
        else
          next('/')
      }
    }
  ]
})