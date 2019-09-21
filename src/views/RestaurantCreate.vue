<template>
  <form class="ui form" @submit.prevent="onCreateClicked">
    <div class="field">
      <label>Restaurnat Name</label>
      <input type="text" placeholder="Restaurnat Name" v-model="restaurant.name" />
    </div>
    <div class="field">
      <label>Address</label>
      <input type="text" placeholder="Address" v-model="restaurant.address" />
    </div>
    <button class="ui button" type="submit">Create</button>
  </form>
</template>


<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      restaurant: {
        name: "",
        address: ""
      }
    };
  },
  methods: {
    ...mapActions(["createRestaurant"]),
    onCreateClicked() {
      this.createRestaurant(this.restaurant).then(({ data }) => {
        this.$router.push(`/restaurants/${data.id}`);
      });
    }
  }
};
</script>