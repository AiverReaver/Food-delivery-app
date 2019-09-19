<template>
  <div id="app">
    <Navbar />
    <div class="ui container">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
export default {
  components: {
    Navbar
  }
};
</script>

<style>
body > .grid {
  height: 100%;
}

.column {
  max-width: 450px;
}
</style>
