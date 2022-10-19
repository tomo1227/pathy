<script setup>
import HeaderBeforeLogin from "@/components/templates/HeaderBeforeLogin";
import HeaderAfterLogin from "@/components/templates/HeaderAfterLogin";
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();
</script>

<template>
  <header>
    <div id="header_containers">
      <HeaderBeforeLogin v-if="store.loginState" />
      <HeaderAfterLogin v-else />
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

header {
  height: 90px;
}

#header_containers {
  display: flex;
  justify-content: space-between;
  color: #000;
  background-color: rgb(251, 192, 82);
  margin: 0;
  padding: 8px 32px 8px;
  width: 100%;
  align-items: stretch;
  box-sizing: border-box;
  align-items: center;
}
/* 
.header_items {
  box-sizing: border-box;
  height: 50%;
} */

/* #header_logo {
  
} */
/* #search_form {
  position: relative;
  max-width: 300px;
  margin-bottom: 20px;
}
#search_box {
  height: 50px;
  padding: 0 10px;
  position: absolute;
  left: 0;
  top: 0;
  border-radius: 25px;
  outline: 0;
  background: #eee;
}
#search_button {
  height: 50px;
  width: 50px;
  position: absolute;
  left: 250px;
  top: 0;
  background: #7fbfff;
  color: #fff;
  border: none;
  border-radius: 0 25px 25px 0;
}
#search_button .fa-search {
  font-size: 20px;
  position: absolute;
  top: 30%;
  left: 30%;
}
#search_button:hover {
  color: #888;
} */
/*
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
} */
</style>
