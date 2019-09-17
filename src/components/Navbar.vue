<template>
  <div>
    <sui-menu secondary>
      <sui-menu-item active link>
        <router-link to="/">Home</router-link>
      </sui-menu-item>
      <sui-menu-item>
        <router-link to="/about">About</router-link>
      </sui-menu-item>
      <sui-menu-menu position="right">
        <sui-menu-item>
          <router-link to="/login">Login</router-link>
        </sui-menu-item>
        <sui-menu-item>
          <router-link to="/register">SignUp</router-link>
        </sui-menu-item>
      </sui-menu-menu>
    </sui-menu>
  </div>
</template>

