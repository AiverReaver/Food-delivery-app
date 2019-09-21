<template>
  <div class="ui cards">
    <div class="card" v-for="food in foods" :key="food.id">
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
</template>

<script>
export default {
  props: ["foods"]
};
</script>