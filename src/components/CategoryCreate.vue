<template>
  <a class="item" v-if="getLoggedInUserRole === 'restaurant'">
    <div class="ui icon input" v-if="isAddingCategory">
      <input type="text" placeholder="Add Category" v-model="category" autofocus />
      <i class="inverted circular plus blue link icon" @click="addCategory"></i>
    </div>
    <button class="ui blue icon button" v-else @click="isAddingCategory = true">
      <i class="plus icon"></i> Add Category
    </button>
  </a>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";
export default {
  props: ["restaurantId"],
  data() {
    return {
      isAddingCategory: false,
      category: ""
    };
  },
  computed: {
    ...mapGetters(["getLoggedInUserRole"])
  },
  methods: {
    ...mapActions(["createCategory"]),

    addCategory() {
      this.createCategory({
        restaurant_id: this.restaurantId,
        category: this.category
      }).then(({ data }) => {
        this.$emit("categoryCreated", data);
      });

      this.category = "";
    }
  }
};
</script>