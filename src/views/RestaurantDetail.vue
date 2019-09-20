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
          <a class="item" v-if="getLoggedInUserRole === 'restaurant'">
            <div class="ui icon input" v-if="isAddingCategory">
              <input
                type="text"
                placeholder="Add Category"
                v-model="category"
                autofocus
                @blur="isAddingCategory = false"
              />
              <i class="inverted circular plus blue link icon" @click="addCategory"></i>
            </div>
            <button class="ui blue icon button" v-else @click="isAddingCategory = true">
              <i class="plus icon"></i> Add Category
            </button>
          </a>
        </div>
      </div>
      <div class="twelve wide column">
        <div class="ui grid">
          <div class="row" v-if="getLoggedInUserRole === 'restaurant'">
            <div v-if="isAddingFood">
              <form class="ui form" @submit.prevent="addFood">
                <div class="field">
                  <input type="text" placeholder="Food Name" v-model="food.name" />
                </div>
                <div class="field">
                  <input type="text" placeholder="Food Price" v-model="food.price" />
                </div>
                <div class="field">
                  <textarea
                    type="text"
                    rows="3"
                    placeholder="Description"
                    v-model="food.description"
                  ></textarea>
                </div>
                <div class="two fields">
                  <div class="field">
                    <div class="ui checkbox">
                      <input type="checkbox" v-model="food.is_veg" />
                      <label>Veg</label>
                    </div>
                  </div>
                  <div class="field">
                    <div class="ui checkbox">
                      <input type="checkbox" v-model="food.active" />
                      <label>In Stock</label>
                    </div>
                  </div>
                </div>
                <div class="two fields">
                  <div class="field">
                    <button class="ui positive button" type="submit">Submit</button>
                  </div>
                  <div class="field">
                    <button
                      class="ui negative basic button"
                      type="button"
                      @click="isAddingFood = false"
                    >Cancel</button>
                  </div>
                </div>
              </form>
            </div>
            <button class="ui blue icon button" v-else @click="isAddingFood = true">
              <i class="plus icon"></i> Add Food
            </button>
          </div>
          <div class="row">
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
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
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
      category: "",
      isAddingCategory: false,
      isAddingFood: false,
      food: {
        name: "",
        description: "",
        price: "",
        active: false,
        is_veg: false
      }
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
    addCategory() {
      this.createCategory({
        restaurant_id: this.restaurant.id,
        category: this.category
      }).then(({ data }) => {
        this.categories.push(data);
      });

      this.category = "";
    },
    addFood() {
      this.createFood({
        restaurant_id: this.restaurant.id,
        category_id: this.selectedCategory.id,
        food: this.food
      }).then(({ data }) => {
        this.categories.forEach((category, index) => {
          console.log(category);
          console.log(this.selectedCategory);
          if (category.id === this.selectedCategory.id) {
            category.foods.push(data);
          }
        });
      });
    }
  }
};
</script>