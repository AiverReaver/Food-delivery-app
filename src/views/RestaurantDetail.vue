<template>
  <div>
    <h1 class="ui header">{{restaurant.name}}</h1>
    <div class="ui grid">
      <div class="four wide column">
        <div class="ui vertical fluid tabular menu">
          <a
            class="item"
            :class="{active: selectedCategory.id === category.id}"
            v-for="category in restaurant.categories"
            :key="category.id"
            @click="changeCategory(category)"
          >{{category.name}}</a>
        </div>
      </div>
      <div class="twelve wide stretched column">
        <div class="ui cards">
          <div class="card" v-for="food in selectedCategory.foods" :key="food.id">
            <div class="content">
              <div class="header">{{food.name}}</div>
              <div class="meta">₹ {{food.price}}</div>
              <div class="description">{{food.description}}</div>
            </div>
            <div class="ui green basic bottom attached button">
              <i class="add icon"></i>
              Add To Cart
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  created() {
    this.getRestaurant(this.$route.params.id).then(({ data }) => {
      this.restaurant = data;
      this.selectedCategory = data.categories[0];
    });
  },
  data() {
    return {
      restaurant: { categories: [] },
      selectedCategory: {}
    };
  },
  methods: {
    ...mapActions(["getRestaurant"]),

    changeCategory(category) {
      this.selectedCategory = category;
    }
  }
};
</script>