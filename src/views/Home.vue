<template>
  <div>
    <div class="ui search">
      <div class="ui icon input">
        <input class="prompt" type="text" placeholder="Search restaurant" v-model="searchQuery" />
        <i class="search icon"></i>
      </div>
    </div>
    <div class="ui cards">
      <div class="card" v-for="restaurant in restaurants" :key="restaurant.id">
        <div class="content">
          <div class="header">{{ restaurant.name }}</div>

          <div class="description">{{restaurant.address}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import search from "@/components/SearchForm.vue";
import axios from "axios";
import { mapState, mapActions } from "vuex";

export default {
  name: "home",

  created() {
    this.getRestaurants();
  },

  components: {
    search
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
