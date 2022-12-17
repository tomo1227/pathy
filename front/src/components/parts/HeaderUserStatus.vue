<script setup>
import { ref } from "vue";

let is0penUserMenu = ref(false);

// クリックしたらflagを反転
const openUserMenu = () => {
  is0penUserMenu.value = !is0penUserMenu.value;
};
</script>

<template>
  <a
    href="#"
    class="header-user-home"
    data-bs-toggle="dropdown"
    aria-expanded="false"
    @click="openUserMenu"
  >
    <img
      id="header-user-icon"
      src="https://github.com/tomo1227.png"
      alt="mdo"
      width="32"
      height="32"
      class="rounded-circle"
    />
  </a>

  <!-- アイコンをクリックしたら表示する -->
  <ul class="dropdown-menu text-small" v-if="is0penUserMenu">
    <li class="dropdown-item">
      <a href="/">あああ</a>
    </li>
    <li class="dropdown-item"><a href="/">設定</a></li>
    <li class="dropdown-item"><a href="/edit">プロフィール</a></li>
    <li class="dropdown-item-line"><hr class="dropdown-line" /></li>
    <li class="dropdown-item"><a href="/logout">ログアウト</a></li>
  </ul>
</template>

<style>
#header-user-icon {
  border-radius: 50%;
}

/* ログイン済のヘッダ、グリッド付きのヘッダ用 */
.dropdown-toggle {
  outline: 0;
}
.dropdown-menu {
  background-color: rgb(255, 255, 255);
  box-shadow: 0px 1px 4px rgb(0 0 0 / 14%);
  display: block;
  min-width: 200px;
  padding: 16px 0;
  position: absolute;
  /* top: 56px; */
  right: 0;
  font-size: 15px;
}

.dropdown-item {
  list-style: none;
  padding: 5px;
}

.dropdown-item:hover {
  background-color: rgb(220, 220, 220);
}

.dropdown-item-line {
  list-style: none;
  margin: 0;
}

.dropdown-item,
a {
  text-decoration: none;
}
</style>
