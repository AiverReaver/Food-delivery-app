<template>
  <sui-grid :centered="true">
    <sui-grid-row>
      <sui-form @submit.prevent="onLoginClicked">
        <h2 is="sui-header">Login</h2>
        <sui-grid-column>
          <sui-form-field>
            <input placeholder="Username" v-model="username" />
          </sui-form-field>

          <sui-form-field>
            <input placeholder="Password" type="password" v-model="password" />
          </sui-form-field>
          <sui-button type="submit">Login</sui-button>
        </sui-grid-column>
      </sui-form>
    </sui-grid-row>
  </sui-grid>
</template>

<script>
import axios from "axios";
export default {
  props: {},
  data() {
    return {
      username: "",
      password: ""
    };
  },

  methods: {
    onLoginClicked() {
      axios
        .post(" http://127.0.0.1:8000/authentication/token/", {
          username: this.username,
          password: this.password
        })
        .then(({ data }) => {
          localStorage.setItem("token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token);
        });
    }
  }
};
</script>