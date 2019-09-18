<template>
  <div class="ui middle aligned centered aligned grid">
    <div class="column">
      <h2 class="ui image header">
        <div class="content">Register for new account</div>
      </h2>
      <form class="ui large form" @submit.prevent="onRegisterClicked">
        <div class="ui stacked segment">
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="Username" v-model="username" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="email" v-model="email" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Password" v-model="password" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="text" placeholder="Confirm password" v-model="confirmPassword" />
            </div>
          </div>
          <input type="submit" value="Register" class="ui fluid large teal submit button" />
        </div>
      </form>

      <div class="ui message">
        already have an account?
        <router-link to="/login">login</router-link>
      </div>
    </div>
  </div>
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