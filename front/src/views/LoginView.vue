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
</script>

<template>
  <div class="login">
    <h1>Login</h1>
    <div class="form-item">
      <label for="email">Email</label>
      <input id="email" autocomplete="off" type="email" v-model="email" />
    </div>
    <div class="form-item">
      <label for="password">Password</label>
      <input
        id="password"
        autocomplete="off"
        type="password"
        v-model="password"
      />
    </div>
    <div class="form-item">
      <button class="submit btn" @click="login">Login</button>
    </div>
  </div>
</template>
