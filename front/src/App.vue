<template>
  <nav class="menu">
    <router-link to="/">Home</router-link> |
    <router-link to="/edit">Editor</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/logout">Logout</router-link>
  </nav>
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
