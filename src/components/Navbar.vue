<template>
  <div class="ui secondary menu">
    <router-link class="item" exact-active-class="active" to="/">Home</router-link>
    <router-link class="item" exact-active-class="active" to="/about">About</router-link>
    <div class="right menu">
      <div class="item">
        <div class="ui icon input">
          <input type="text" placeholder="Search..." />
          <i class="search link icon"></i>
        </div>
      </div>
      <router-link class="item" exact-active-class="active" to="/login">Login</router-link>
      <router-link class="item" exact-active-class="active" to="/register">SignUp</router-link>
    </div>
  </div>
</template>

