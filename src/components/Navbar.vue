<template>
  <div class="ui secondary menu">
    <router-link class="item" exact-active-class="active" to="/">Home</router-link>
    <router-link
      v-if="getLoggedInUserRole === 'restaurant'"
      class="item"
      exact-active-class="active"
      to="/create"
    >Create Restaurant</router-link>
    <div class="right menu">
      <a class="item" v-if="isLoggedIn" @click="logout">Logout</a>
      <router-link v-if="!isLoggedIn" class="item" exact-active-class="active" to="/login">Login</router-link>
      <div class="item" v-if="!isLoggedIn">
        <router-link class="ui primary button" exact-active-class="active" to="/register">SignUp</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions, mapGetters } from "vuex";
export default {
  methods: {
    ...mapActions(["logoutUser"]),
    logout() {
      this.$router.replace("/");
      this.logoutUser();
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn", "getLoggedInUserRole"])
  }
};
</script>

