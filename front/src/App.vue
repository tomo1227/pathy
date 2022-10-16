<script setup>
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();
</script>

<template>
  <header>
    <div class="header__inner">
      <h3 class="header__title header-title">
        <a href="/">
          <img alt="Pathy ロゴ" src="@/assets/header_logo.png" width="100" />
        </a>
      </h3>
      <nav class="menu">
        <router-link to="/" v-show="store.loginState">Home</router-link> |
        <router-link to="/edit" v-show="store.loginState">Editor</router-link> |
        <router-link to="/login" v-show="!store.loginState">Login</router-link>
        |
        <router-link to="/logout" v-show="store.loginState">Logout</router-link>
      </nav>
    </div>
  </header>
  <router-view />
</template>

<style>
html {
  height: 100%;
}

body {
  margin: 0;
  height: 100%;
}

#app {
  margin: 0;
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav,
menu {
  display: block;
  margin: 0;
  height: 10px;
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
