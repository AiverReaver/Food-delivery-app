import Vue from 'vue';
import Vuex from 'vuex';
import foodDelivery from './api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    restaurants: [],
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refresh_token'),
    role: localStorage.getItem('role')
  },
  mutations: {
    setRestaurants(state, restaurants) {
      state.restaurants = restaurants;
    },

    setToken(state, token) {
      state.token = token;
    },

    setRefreshToken(state, token) {
      state.refreshToken = token;
    },

    setRole(state, role) {
      state.role = role;
    }
  },
  actions: {
    async getRestaurants({
      commit
    }, search) {
      const {
        data
      } = await foodDelivery.get('/restaurants/', {
        params: {
          search
        }
      });

      commit('setRestaurants', data);
    },

    createRestaurant(context, restaurant) {
      return foodDelivery.post('/restaurants/', restaurant);
    },

    getRestaurant(context, id) {
      return foodDelivery.get(`/restaurants/${id}`);
    },

    createCategory(context, payload) {
      return foodDelivery.post(
        `/restaurants/${payload.restaurant_id}/categories/`, {
          name: payload.category
        }
      );
    },

    createFood(context, payload) {
      return foodDelivery.post(
        `/restaurants/${payload.restaurant_id}/categories/${payload.category_id}/foods/`,
        payload.food
      );
    },

    setTokens({
      commit
    }, data) {
      foodDelivery.defaults.headers[
        'Authorization'
      ] = `Bearer ${data.access_token}`;

      commit('setRole', data.user_role);
      commit('setToken', data.access_token);
      commit('setRefreshToken', data.refresh_token);

      localStorage.setItem('token', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      localStorage.setItem('role', data.user_role);
    },

    loginUser(context, user) {
      return foodDelivery.post('/authentication/token/', user);
    },

    registerUser(context, user) {
      return foodDelivery.post('/authentication/register/customer', user);
    },

    registerRestaurant(context, user) {
      return foodDelivery.post('/authentication/register/restaurant', user);
    },

    async logoutUser({
      commit,
      state
    }) {
      await foodDelivery.post('/authentication/token/revoke/', {
        token: state.token
      });

      commit('setRole', 'customer');
      commit('setToken', null);
      commit('setRefreshToken', null);
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('role');
    }
  },

  getters: {
    isLoggedIn(state) {
      return state.token !== null;
    },
    getLoggedInUserRole(state) {
      return state.role;
    }
  }
});