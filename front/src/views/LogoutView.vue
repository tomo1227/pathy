<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const store = useAuthStore();

// ログアウト → ログイン画面へ
const logout = () => {
  store.logout();
  router.push("/login");
};

// ログアウトしない → Home画面へ
const nologout = () => {
  router.push("/");
};
</script>

<template>
  <div class="logout form-container">
    <h1>Logout</h1>
    <hr />
    <h2>ログアウトしますか？</h2>
    <div class="form-item">
      <button class="form-button cancelbtn" @click="nologout">NO</button>
      <button class="form-button signupbtn" @click="logout">YES</button>
    </div>
  </div>
</template>
