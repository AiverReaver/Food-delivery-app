<template>
  <div class="ui middle aligned centered aligned grid">
    <div class="column">
      <h2 class="ui image header" v-if="isRestaurant">
        <div class="content">Register new restaurant</div>
      </h2>
      <h2 class="ui image header" v-else>
        <div class="content">Register for new account</div>
      </h2>
      <form class="ui large form" @submit.prevent="onRegisterClicked">
        <div class="ui stacked segment">
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input
                type="text"
                :placeholder="isRestaurant ? 'Restaurant Name': 'Username'"
                v-model="user.username"
              />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="email" v-model="user.email" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Password" v-model="user.password" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Confirm password" v-model="user.confirmPassword" />
            </div>
          </div>
          <input
            v-if="isRestaurant"
            type="submit"
            value="Register as restaurant"
            class="ui fluid large teal submit button"
          />
          <input v-else type="submit" value="Register" class="ui fluid large teal submit button" />
        </div>
      </form>

      <div class="ui message">
        already have an account?
        <router-link to="/login">login</router-link>
      </div>
      <div class="ui message" v-if="isRestaurant">
        register as customer?
        <a href @click.prevent="isRestaurant=false">register</a>
      </div>
      <div class="ui message" v-else>
        register as restuarant?
        <a href @click.prevent="isRestaurant=true">register</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      user: { username: "", email: "", password: "", confirmPassword: "" },
      isRestaurant: false
    };
  },
  methods: {
    ...mapActions(["registerUser", "registerRestaurant", "setTokens"]),
    onRegisterClicked() {
      if (this.isRestaurant) {
        this.registerRestaurant(this.user)
          .then(({ data }) => {
            this.$router.push("/");
            this.setTokens(data);
          })
          .catch(error => {
            console.error(error);
          });
      } else {
        this.registerUser(this.user)
          .then(({ data }) => {
            this.$router.push("/");
            this.setTokens(data);
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  }
};
</script>