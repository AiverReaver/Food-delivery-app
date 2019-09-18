<template>
  <div class="ui search">
    <div class="ui icon input">
      <input
        class="prompt"
        type="text"
        :placeholder="placeholder"
        v-model="searchQuery"
        @keypress="onInputChange"
      />
      <i class="search icon"></i>
    </div>
    <!-- <div class="results transition visible" style="display: block !important;">
      <a class="result">
        <div class="content">
          <div class="title">password</div>
        </div>
      </a>
    </div>-->
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      searchQuery: ""
    };
  },
  props: {
    placeholder: String
  },
  methods: {
    onInputChange(e) {
      axios.get().then(({ candidates }) => {
        console.log(candidates);
      });
    }
  }
};
</script>