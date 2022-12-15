<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const email = ref("");
const password = ref("");
const router = useRouter();
const store = useAuthStore();
const errorNotFound = ref(false);
const errorMessage = ref({
  username: false,
  email: false,
  password: false,
  re_password: false,
});

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
      if (error.response?.status == 400) {
        if (error.response.data) {
          // validation
          const errorData = error.response.data;
          errorMessage.value.email = errorData.email
            ? errorData.email[0]
            : false;
          errorMessage.value.password = errorData.password
            ? errorData.password[0]
            : false;
        }
      } else if (error.response?.status == 401) {
        if (error.response.data) {
          errorNotFound.value = "メールアドレスかパスワードが間違っています。";
        }
      }
    });
};

const signUp = () => {
  router.push("/signUp");
};
</script>

<template>
  <div class="login form-container">
    <h1>Login</h1>
    <hr />
    <p class="margin_zero validation-form" v-show="errorNotFound">
      {{ errorNotFound }}
    </p>
    <div class="form-group">
      <label for="Email">Email</label>
      <p class="margin_zero validation-form" v-show="errorMessage.email">
        {{ errorMessage.email }}
      </p>
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
      <p class="margin_zero validation-form" v-show="errorMessage.password">
        {{ errorMessage.password }}
      </p>
      <input
        id="password"
        class="form-control"
        autocomplete="off"
        type="password"
        v-model="password"
        placeholder="パスワード"
      />
    </div>
    <button type="button" class="btn btn-primary form-button" @click="login">
      Login
    </button>
    <p>登録がまだの人は新規登録！</p>
    <button
      type="button"
      class="btn btn-primary bluebtn form-button"
      @click="signUp"
    >
      新規登録
    </button>
  </div>
</template>
