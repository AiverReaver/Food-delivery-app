<template>
  <div class="ui secondary menu">
    <router-link class="item" exact-active-class="active" to="/">Home</router-link>
    <router-link class="item" exact-active-class="active" to="/about">About</router-link>
    <div class="right menu">
      <div class="item">
        <div class="ui icon input">
          <input type="text" placeholder="Search..." />
          <i class="search link icon"></i>
        </div>
      </div>

      <button class="item" v-if="isLoggedIn()" @click="logout">Logout</button>
      <router-link v-if="!isLoggedIn()" class="item" exact-active-class="active" to="/login">Login</router-link>
      <div class="item" v-if="!isLoggedIn()">
        <router-link class="ui primary button" exact-active-class="active" to="/register">SignUp</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  methods: {
    isLoggedIn() {
      return localStorage.getItem("token") !== "";
    },

    logout() {
      axios
        .post("http://127.0.0.1:8000/authentication/token/revoke/", {
          token: localStorage.getItem("token")
        })
        .then(res => {
          localStorage.removeItem("token");
          localStorage.removeItem("refresh_token");
        });
    }
  }
};
</script>

