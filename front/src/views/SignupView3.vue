<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
// import { useAuthStore } from "@/stores/auth";

const username = ref("");
const email = ref("");
const password = ref("");
const password2 = ref("");
const router = useRouter();
// const store = useAuthStore();

const submitSignUp = () => {
  axios
    .post("auth/users/", {
      username: username.value,
      email: email.value,
      password: password.value,
      re_password: password2.value,
    })
    .then((response) => {
      //   store.login(email.value, response.data.access, response.data.refresh);
      router.push("/last-signup");
      console.log(response);
    })
    .catch((error) => {
      if (error.response?.status != 200) {
        // router.push("/login");
        if (
          error.response.data.email[0] ===
          "この メールアドレス を持った my user が既に存在します。"
        ) {
          console.error("このメールアドレスは既に使われております。");
        }
      }
    });
};

const cancelSignUp = () => {
  router.push("/signUp");
};
</script>

<template>
  <div class="login">
    <h1>Login</h1>
    <div class="form-group">
      <label for="username">UserID</label>
      <input
        class="form-control"
        id="username"
        autocomplete="on"
        type="text"
        v-model="username"
        placeholder="ユーザID"
        required="入力必須です"
      />
      <!-- </div> -->

      <!-- <div class="form-group"> -->
      <label for="Email">Email</label>
      <input
        class="form-control"
        id="email"
        autocomplete="on"
        type="email"
        v-model="email"
        placeholder="メールアドレス"
        required="入力必須です"
      />
      <!-- </div> -->
      <!-- <div class="form-group"> -->
      <label for="password">Password</label>
      <input
        id="password"
        class="form-control"
        autocomplete="off"
        type="password"
        v-model="password"
        placeholder="パスワード"
        required="入力必須です。"
      />
      <!-- </div> -->
      <!-- <div class="form-group"> -->
      <label for="password2">Password 確認</label>
      <input
        class="form-control"
        id="password2"
        autocomplete="on"
        type="password"
        v-model="password2"
        placeholder="メールアドレス"
        required="入力必須です。"
      />
    </div>
    <button type="button" class="cancelbtn" @click="cancelSignUp">
      Cancel
    </button>
    <button type="button" class="signupbtn" @click="submitSignUp">
      新規登録
    </button>
  </div>
</template>

<style>
input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}
</style>
