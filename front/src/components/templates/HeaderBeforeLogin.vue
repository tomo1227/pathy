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
    <!-- ログイン前 begin-->
    <nav class="menu">
      <router-link to="/login"> Login</router-link>
    </nav>
    <!-- ログイン前 end -->
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
    <div id="header_login">
      <!-- ログイン前 begin-->
      <nav class="menu">
        <router-link to="/login"> Login</router-link>
      </nav>
      <!-- ログイン前 end -->
    </div>
  </div>
</template>

.header_items { box-sizing: border-box; height: 50%; }
