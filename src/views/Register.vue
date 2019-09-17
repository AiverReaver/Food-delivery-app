<template>
  <sui-grid :centered="true">
    <sui-grid-row>
      <sui-form @submit.prevent="onRegisterClicked">
        <h2 is="sui-header">Register</h2>
        <sui-grid-column>
          <sui-form-field>
            <input placeholder="Username" v-model="username" />
          </sui-form-field>
          <sui-form-field>
            <input placeholder="email" v-model="email" />
          </sui-form-field>
          <sui-form-field>
            <input placeholder="Password" type="password" v-model="password" />
          </sui-form-field>
          <sui-form-field>
            <input placeholder="Confirm Password" type="password" v-model="confirmPassword" />
          </sui-form-field>
          <sui-button type="submit">register</sui-button>
        </sui-grid-column>
      </sui-form>
    </sui-grid-row>
  </sui-grid>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: ""
    };
  },
  methods: {
    onRegisterClicked() {
      axios
        .post(" http://127.0.0.1:8000/authentication/register/", {
          username: this.username,
          email: this.email,
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