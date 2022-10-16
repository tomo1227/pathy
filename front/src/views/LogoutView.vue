<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const store = useAuthStore();

const logout = () => {
  // ログアウトしたら、ログイン画面へ
  store.logout();
  router.push("/login");
};

const nologout = () => {
  // ログアウトしないなら、Home画面へ
  router.push("/");
};
</script>

<template>
  <div class="logout">
    <h1>ログアウトしますか？</h1>
    <div class="form-item">
      <button class="submit btn" @click="logout">YES</button>
      <button class="submit btn" @click="nologout">NO</button>
    </div>
  </div>
</template>
