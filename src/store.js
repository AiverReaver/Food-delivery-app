import Vue from 'vue';
import Vuex from 'vuex';
import foodDelivery from './api';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    restaurants: [],
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refresh_token')
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
    }
  },
  actions: {
    async getRestaurants({
      commit
    }, search) {
      const {
        data
      } =
      await foodDelivery.get('/restaurants/', {
        params: {
          search
        }
      });

      commit('setRestaurants', data);
    },
    setTokens({
      commit
    }, data) {
      foodDelivery.defaults.headers['Authorization'] = `Bearer ${data.access_token}`;
      commit('setToken', data.access_token)
      commit('setRefreshToken', data.refresh_token)
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("refresh_token", data.refresh_token);
    },
    async loginUser({
      dispatch
    }, user) {
      const {
        data
      } = await foodDelivery.post('/authentication/token/', user);
      dispatch('setTokens', data);
    },
    async registerUser({
      dispatch
    }, user) {
      const {
        data
      } = await foodDelivery.post('/authentication/register/', user);
      dispatch('setTokens', data);
    },
    async logoutUser({
      commit,
      state
    }) {
      const {
        data
      } = await foodDelivery.post('/authentication/token/revoke/', {
        token: state.token
      });

      console.log(data.message);
      commit('setToken', null)
      commit('setRefreshToken', null)
      localStorage.removeItem("token");
      localStorage.removeItem("refresh_token");
    }
  },
  getters: {
    isLoggedIn(state) {
      return state.token !== null;
    }
  }
});