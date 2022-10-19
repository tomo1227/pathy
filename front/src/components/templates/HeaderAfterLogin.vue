<script setup>
import HeaderLogo from "@/components/parts/HeaderLogo";
</script>

<template>
  <div id="header_logo" class="header_items">
    <HeaderLogo />
  </div>
  <div id="header_menu" class="header_items">
    <!-- ログイン後 begin-->
    <nav class="menu">
      <router-link to="/">Home</router-link>
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
    <div id="header_login">
      <!-- ログイン後 begin -->
      <nav class="menu">
        <router-link to="/logout">ログアウト</router-link>
        <!-- ログイン後 end-->
      </nav>
    </div>
  </div>
</template>

.header_items { box-sizing: border-box; height: 50%; }
