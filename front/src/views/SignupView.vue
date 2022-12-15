<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
// import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const username = ref("");
const email = ref("");
const password = ref("");
const re_password = ref("");
const errorMessage = ref({
  username: false,
  email: false,
  password: false,
  re_password: false,
});

const submitSignUp = () => {
  // const store = useAuthStore();
  const input = new URLSearchParams();

  input.append("username", username.value);
  input.append("email", email.value);
  input.append("password", password.value);
  input.append("re_password", re_password.value);

  createUser(input);
};

const createUser = (params) => {
  axios
    .post("auth/users/", params)
    .then((response) => {
      console.log(response);
      // store.login(email.value, response.data.access, response.data.refresh);
      router.push("/last-signup");
    })
    .catch((error) => {
      if (error.response?.status == 400) {
        if (error.response.data) {
          // validation
          const errorData = error.response.data;
          errorMessage.value.username = errorData.username
            ? errorData.username[0]
            : false;
          errorMessage.value.email = errorData.email
            ? errorData.email[0]
            : false;
          errorMessage.value.password = errorData.password
            ? errorData.password[0]
            : false;
          errorMessage.value.re_password = errorData.re_password
            ? errorData.re_password[0]
            : false;
        }
      }
    });
};
const cancelSignUp = () => {
  router.push("/");
};
</script>

<template>
  <form style="border: 1px solid #ccc">
    <div class="form-container">
      <h1>新規登録</h1>
      <!-- <p>Please fill in this form to create an account.</p> -->
      <hr />
      <label for="username"><b>username</b></label>
      <p class="margin_zero validation-form" v-show="errorMessage.username">
        {{ errorMessage.username }}
      </p>
      <input
        class="form-control"
        type="text"
        placeholder="Enter UserID"
        autocomplete="on"
        v-model="username"
      />
      <label for="email"><b>Email</b></label>
      <p class="margin_zero validation-form" v-show="errorMessage.email">
        {{ errorMessage.email }}
      </p>
      <input
        class="form-control"
        type="email"
        placeholder="Enter Email"
        autocomplete="on"
        v-model="email"
      />
      <label for="psw"><b>Password</b></label>
      <p class="margin_zero validation-form" v-show="errorMessage.password">
        {{ errorMessage.password }}
      </p>
      <input
        class="form-control"
        type="password"
        placeholder="Enter Password"
        autocomplete="off"
        v-model="password"
        required
      />
      <label for="psw-repeat"><b>Repeat Password</b></label>
      <p class="margin_zero validation-form" v-show="errorMessage.re_password">
        {{ errorMessage.re_password }}
      </p>
      <input
        class="form-control"
        type="password"
        placeholder="Repeat Password"
        v-model="re_password"
        required
      />
      <div class="clearfix">
        <button
          type="button"
          class="form-button cancelbtn"
          @click="cancelSignUp"
        >
          Cancel
        </button>
        <button
          type="button"
          class="signupbtn form-button"
          @click="submitSignUp"
        >
          Sign Up
        </button>
      </div>
    </div>
  </form>
</template>

<style>
/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
</style>
