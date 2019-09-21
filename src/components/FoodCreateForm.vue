<template>
  <div v-if="getLoggedInUserRole === 'restaurant'">
    <div v-if="isAddingFood">
      <form class="ui form" @submit.prevent="addFood">
        <div class="field">
          <input type="text" placeholder="Food Name" v-model="food.name" />
        </div>
        <div class="field">
          <input type="text" placeholder="Food Price" v-model="food.price" />
        </div>
        <div class="field">
          <textarea type="text" rows="3" placeholder="Description" v-model="food.description"></textarea>
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
</template>

<script>
import { mapGetters, mapActions, mapMutations, mapState } from "vuex";
export default {
  props: ["restaurantId", "categoryId"],
  data() {
    return {
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
    ...mapGetters(["getLoggedInUserRole"]),
    ...mapState({
      categories: "selecatedRestaurantcategories"
    })
  },
  methods: {
    ...mapActions(["createFood"]),

    addFood() {
      this.createFood({
        restaurant_id: this.restaurantId,
        category_id: this.categoryId,
        food: this.food
      }).then(({ data }) => {
        this.$emit("foodCreated", data);
      });

      this.food = {
        name: "",
        description: "",
        price: "",
        active: false,
        is_veg: false
      };
    }
  }
};
</script>