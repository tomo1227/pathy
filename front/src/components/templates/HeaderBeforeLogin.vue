<script setup>
import HeaderLogo from "@/components/parts/HeaderLogo";
import HeaderSearchBox from "@/components/parts/HeaderSearchBox";
</script>

<template>
  <div id="header_logo" class="header_items">
    <HeaderLogo />
  </div>
  <div id="header_menu" class="header_items">
    <!-- ログイン前 begin-->
    <nav>
      <ul class="menu_list">
        <li class="menu_item">
          <router-link to="/edit" class="header_link">Login</router-link>
        </li>
      </ul>
      <!-- ログイン前 end-->
    </nav>
  </div>
  <div id="header_status" class="header_items">
    <div id="header_search">
      <HeaderSearchBox />
    </div>
    <div id="header_logout">
      <!-- ログイン前 begin -->
      <nav class="logout_btn">
        <router-link to="/logout" id="logout_btn">Login</router-link>
        <!-- ログイン前 end-->
      </nav>
    </div>
  </div>
</template>

<style>
.header_items {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  height: 50%;
}

#header_login {
  display: box;
}

#logout_btn {
  padding: 5px;
}
</style>
