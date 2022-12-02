<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const email = ref("");
const password = ref("");
const router = useRouter();
const store = useAuthStore();

const login = () => {
  axios
    .post("auth/jwt/create", {
      email: email.value,
      password: password.value,
    })
    .then((response) => {
      store.login(email.value, response.data.access, response.data.refresh);
      router.push("/");
    })
    .catch((error) => {
      if (error.response?.status != 200) {
        router.push("/login");
      }
    });
};

const signUp = () => {
  router.push("/signUp");
};
</script>

<template>
  <div class="login">
    <h1>Login</h1>
    <div class="form-group">
      <label for="Email">Email</label>
      <input
        class="form-control"
        id="email"
        autocomplete="on"
        type="email"
        v-model="email"
        placeholder="メールアドレス"
      />
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input
        id="password"
        class="form-control"
        autocomplete="off"
        type="password"
        v-model="password"
        placeholder="パスワード"
      />
    </div>
    <button type="button" class="btn btn-primary" @click="login">Login</button>
    <p>登録がまだの人はこちら</p>
    <button type="button" class="btn btn-primary" @click="signUp">
      新規登録
    </button>
  </div>
</template>
