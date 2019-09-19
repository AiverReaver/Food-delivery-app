<template>
  <div class="ui middle aligned centered aligned grid">
    <div class="column">
      <h2 class="ui image header">
        <div class="content">Log-in to your account</div>
      </h2>
      <form class="ui large form" @submit.prevent="onLoginClicked">
        <div class="ui stacked segment">
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="Username" v-model="user.username" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Password" v-model="user.password" />
            </div>
          </div>
          <input type="submit" value="Login" class="ui fluid large teal submit button" />
        </div>
      </form>

      <div class="ui message">
        New to us?
        <router-link to="/register">Sign Up</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      user: { username: "", password: "" }
    };
  },

  methods: {
    ...mapActions(["loginUser", "setTokens"]),
    onLoginClicked() {
      this.loginUser(this.user)
        .then(({ data }) => {
          this.$router.push("/");
          this.setTokens(data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
