<script setup>
import HeaderLogo from "@/components/parts/HeaderLogo";
import HeaderSearchBox from "@/components/parts/HeaderSearchBox";
import HeaderUserStatus from "@/components/parts/HeaderUserStatus";
</script>

<template>
  <div id="header_logo" class="header_items">
    <HeaderLogo />
  </div>
  <div id="header_menu" class="warrper header_items header_menu__wrapper">
    <!-- ログイン後 begin-->
    <nav>
      <ul class="warrper menu_list menu_list__wrapper">
        <li class="menu_item">
          <router-link to="/" class="header_link">Home</router-link>
        </li>
        <li class="menu_item">
          <router-link to="/edit" class="header_link">Editor</router-link>
        </li>
        <li class="menu_item">
          <router-link to="/logout" class="header_link">Logout</router-link>
        </li>
      </ul>
      <!-- ログイン後 end-->
    </nav>
  </div>
  <div id="header_status" class="header_items header_status__wrapper">
    <div id="header_search" class="header_status__item">
      <HeaderSearchBox />
    </div>
    <div id="header_user_status" class="dropdown text-end header_status__item">
      <HeaderUserStatus />
    </div>
  </div>
</template>

<style>
.warrper {
  max-width: 1170px;
}

.header_items {
  box-sizing: border-box;
  height: 50%;
  flex: 1;
}

/* #header_logo {
  padding: 0px 100px 0px 0px;
} */

.header_menu__wrapper {
  justify-content: center;
}
@media screen and (max-width: 560px) {
  .header_menu__wrapper {
    order: 2;
    flex: 1 0 100%;
    margin: 0rem -1rem -1rem -1rem;
  }
}

.header_status__wrapper {
  justify-content: flex-end;
  display: flex;
  align-items: center;
}

#header_search {
  display: flex;
  align-items: center;
}

#header_user_status {
  position: relative;
  padding: 0 0.5rem 0;
}

.menu_list {
  display: flex;
  padding: 0px;
  /* justify-content: center;
  flex: 1; */
}

.menu_item {
  padding: 10px 10px;
  list-style: none;
  width: 10em;
}

@media screen and (max-width: 560px) {
  .menu_item {
    width: 7rem;
  }
}

.header_link {
  color: rgb(86, 25, 241);
  font-size: 20px;
  font-weight: 800;
  text-transform: uppercase;
  text-decoration: none;
}

.header_link:hover {
  color: #26c828;
}

#header_logout {
  display: flex;
  align-items: center;
}

#logout_btn {
  color: rgb(86, 25, 241);
  font-size: 15px;
  font-weight: 800;
  text-decoration: none;
}

#logout_btn:hover {
  color: #26c828;
}
</style>
