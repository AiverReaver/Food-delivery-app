<template>
  <div>
    <div class="ui search">
      <div class="ui icon input">
        <input class="prompt" type="text" placeholder="Search restaurant" v-model="searchQuery" />
        <i class="search icon"></i>
      </div>
    </div>
    <div class="ui divider"></div>
    <RestaurantList :restaurants="restaurants" />
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from "vuex";

import RestaurantList from "@/components/RestaurantList.vue";

export default {
  name: "home",

  created() {
    this.getRestaurants();
  },

  components: {
    RestaurantList
  },

  data() {
    return {
      searchQuery: ""
    };
  },

  computed: {
    ...mapState(["restaurants"])
  },

  methods: {
    ...mapActions(["getRestaurants"])
  },

  watch: {
    searchQuery() {
      this.getRestaurants(this.searchQuery);
    }
  }
};
</script>
