<template>
  <div>
    <h1 class="ui header">{{restaurant.name}}</h1>
    <p>{{restaurant.address}}</p>
    <div class="ui grid">
      <div class="four wide column">
        <div class="ui vertical fluid tabular menu">
          <a
            v-for="category in categories"
            class="item"
            :class="{active: selectedCategory.id === category.id}"
            :key="category.id"
            @click="changeCategory(category)"
          >{{category.name}}</a>
          <CategoryCreate :restaurantId="restaurant.id" @categoryCreated="addCategory" />
        </div>
      </div>
      <div class="twelve wide column">
        <div class="ui grid" v-if="categories.length > 0">
          <div class="row">
            <FoodCreateForm
              @foodCreated="addFood"
              :restaurantId="restaurant.id"
              :categoryId="selectedCategory.id"
            />
          </div>
          <div class="row">
            <FoodCardList :foods="selectedCategory.foods" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import CategoryCreate from "@/components/CategoryCreate.vue";
import FoodCreateForm from "@/components/FoodCreateForm.vue";
import FoodCardList from "@/components/FoodCardList.vue";

export default {
  components: {
    FoodCreateForm,
    CategoryCreate,
    FoodCardList
  },
  created() {
    this.getRestaurant(this.$route.params.id).then(({ data }) => {
      this.restaurant = data;
      if (data.categories !== undefined) {
        this.categories = data.categories;
        if (data.categories.length > 0)
          this.selectedCategory = data.categories[0];
      }
    });
  },
  data() {
    return {
      restaurant: {},
      categories: [],
      selectedCategory: { id: 0, foods: [] },
      isAddingCategory: false,
      isAddingFood: false
    };
  },
  computed: {
    ...mapGetters(["getLoggedInUserRole"])
  },
  methods: {
    ...mapActions(["getRestaurant", "createCategory", "createFood"]),

    changeCategory(category) {
      this.selectedCategory = category;
    },
    addCategory(category) {
      this.categories.push(category);
      this.selectedCategory = category;

      this.category = "";
    },
    addFood(food) {
      this.categories.forEach((category, index) => {
        if (category.id === this.selectedCategory.id) {
          category.foods.push(food);
        }
      });
    }
  }
};
</script>