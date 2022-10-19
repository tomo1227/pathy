<script setup>
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();
</script>

<template>
  <div id="header_logo" class="header_items">
    <a href="/">
      <img alt="Pathy ロゴ" src="@/assets/header_logo.png" width="100" />
    </a>
  </div>
  <div id="header_menu" class="header_items">
    <!-- ログイン後 begin-->
    <nav class="menu" v-show="store.loginState">
      <router-link to="/" v-show="store.loginState">Home</router-link>
      <router-link to="/edit">Editor</router-link>
      <router-link to="/logout">Logout</router-link>
      <!-- ログイン後 end-->
    </nav>
  </div>
  <div id="header_status" class="header_items">
    <div class="search">
      <form id="search_form" action="自分のサイトURL" method="get">
        <input id="search_box" type="text" placeholder="検索" />
        <button id="search_button" type="submit">
          <i class="fas fa-search"></i>
        </button>
      </form>
    </div>
    <div id="header_login" v-show="!store.loginState">
      <!-- ログイン後 begin -->
      <nav class="menu" v-show="store.loginState">
        <router-link to="/logout">ログアウト</router-link>
        <!-- ログイン後 end-->
      </nav>
    </div>
  </div>
</template>

.header_items { box-sizing: border-box; height: 50%; }
