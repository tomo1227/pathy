<script setup>
import { useRouter } from "vue-router";
import axios from "axios";
const router = useRouter();

const activation = () => {
  const uid = router.currentRoute.value.params.uid;
  const token = router.currentRoute.value.params.token;
  axios
    .get(`auth/users/activation/${uid}/${token}`)
    .then((response) => {
      if (response?.status == 204) {
        flag = true;
        router.push("/login");
      }
    })
    .catch((error) => {
      if (error.response?.status != 200) {
        // router.push("/login");
        console.error("このメールアドレスは既に使われております。");
      }
    });
};
</script>

<template>
  <div>
    <p>ボタンを押すと登録が完了し、自動的にログインページへと変わります。</p>
    <button type="button" class="btn btn-primary" @click="activation">
      本登録する
    </button>
  </div>
</template>
