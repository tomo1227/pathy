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
      if (error.response?.status != 200) {
        console.warn(error.response?.status);
        console.log(error.config);
        console.log(error);
        // router.push("/");
      }
    });
};
const cancelSignUp = () => {
  router.push("/");
};
</script>

<template>
  <form style="border: 1px solid #ccc">
    <div class="container">
      <h1>新規登録</h1>
      <!-- <p>Please fill in this form to create an account.</p> -->
      <hr />
      <label for="username"><b>username</b></label>
      <input
        type="text"
        placeholder="Enter UserID"
        autocomplete="on"
        v-model="username"
        required
      />

      <label for="email"><b>Email</b></label>
      <input
        type="email"
        placeholder="Enter Email"
        autocomplete="on"
        v-model="email"
        required
      />

      <label for="psw"><b>Password</b></label>
      <input
        type="password"
        placeholder="Enter Password"
        autocomplete="off"
        v-model="password"
        required
      />

      <label for="psw-repeat"><b>Repeat Password</b></label>
      <input
        type="password"
        placeholder="Repeat Password"
        v-model="re_password"
        required
      />
      <div class="clearfix">
        <button type="button" class="cancelbtn" @click="cancelSignUp">
          Cancel
        </button>
        <button type="button" class="signupbtn" @click="submitSignUp">
          Sign Up
        </button>
      </div>
    </div>
  </form>
</template>

<style>
* {
  box-sizing: border-box;
}

/* Full-width input fields */
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

hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for all buttons */
button {
  background-color: #04aa6d;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

button:hover {
  opacity: 1;
}

/* Extra styles for the cancel button */
.cancelbtn {
  padding: 14px 20px;
  background-color: #f44336;
}

/* Float cancel and signup buttons and add an equal width */
.cancelbtn,
.signupbtn {
  float: left;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn,
  .signupbtn {
    width: 100%;
  }
}
</style>
