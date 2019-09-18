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

export default {
  name: "home",

  created() {
    this.getRastaurants();
  },
  components: {
    search
  },
  data() {
    return {
      restaurants: [],
      searchQuery: ""
    };
  },
  methods: {
    getRastaurants(search) {
      axios
        .get(`http://127.0.0.1:8000/api/restaurants/`, {
          params: {
            search
          }
        })
        .then(({ data }) => {
          this.restaurants = data;
        });
    }
  },
  watch: {
    searchQuery() {
      this.getRastaurants(this.searchQuery);
    }
  }
};
</script>
