<template>
  <div class="ui cards">
    <div class="card" v-for="restaurant in restaurants" :key="restaurant.id">
      <div class="content">
        <div class="header">
          <router-link :to="`/restaurants/${restaurant.id}`">{{ restaurant.name }}</router-link>
        </div>

        <div class="description">{{restaurant.address}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["restaurants"]
};
</script>