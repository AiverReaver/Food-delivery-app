<template>
  <div>
    <h1 class="ui header">{{restaurant.name}}</h1>
    <p>{{restaurant.address}}</p>
    <div class="ui grid" v-if="categories.length > 0">
      <div class="four wide column">
        <div class="ui vertical fluid tabular menu">
          <a
            v-for="category in categories"
            class="item"
            :class="{active: selectedCategory.id === category.id}"
            :key="category.id"
            @click="changeCategory(category)"
          >{{category.name}}</a>
          <a class="item" v-hasRole="'restaurant'">
            <div>
              <div class="ui action input">
                <input type="text" placeholder="Add Category" v-model="category" />
                <button class="ui icon button" @click="addCategory">
                  <i class="plus icon"></i>
                </button>
              </div>
            </div>
          </a>
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
      if (data.categories !== undefined) {
        this.categories = data.categories;
        this.selectedCategory = data.categories[0];
      }
    });
  },
  data() {
    return {
      restaurant: {},
      categories: [],
      selectedCategory: { foods: [] },
      category: ""
    };
  },
  methods: {
    ...mapActions(["getRestaurant", "createCategory"]),

    changeCategory(category) {
      this.selectedCategory = category;
    },
    addCategory() {
      this.createCategory({
        id: this.restaurant.id,
        category: this.category
      }).then(({ data }) => {
        this.categories.push(data);
      });
    }
  }
};
</script>