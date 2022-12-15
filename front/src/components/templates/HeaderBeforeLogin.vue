<script setup>
import HeaderLogo from "@/components/parts/HeaderLogo";
import HeaderSearchBox from "@/components/parts/HeaderSearchBox";
</script>

<template>
  <div id="header_logo" class="header_items">
    <HeaderLogo />
  </div>
  <div id="header_status" class="header_items header_status__wrapper">
    <div id="header_search">
      <HeaderSearchBox />
    </div>
    <div id="header_logout">
      <!-- ログイン前 begin -->
      <nav class="login_btn">
        <router-link to="/login" id="login_btn">Login</router-link>
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

#login_btn {
  padding: 5px;
  margin-left: auto;
}
</style>
