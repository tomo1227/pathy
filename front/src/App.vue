<script setup>
import HeaderBeforeLogin from "@/components/templates/HeaderBeforeLogin";
import HeaderAfterLogin from "@/components/templates/HeaderAfterLogin";
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();
</script>

<template>
  <header>
    <div id="header_containers">
      <HeaderBeforeLogin v-if="!store.loginState" />
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
</style>
