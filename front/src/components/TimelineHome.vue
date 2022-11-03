<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { storeToRefs } from "pinia";

const articles = ref([]);
const store = useAuthStore();
const { accessToken } = storeToRefs(store);
const { refreshToken } = storeToRefs(store);
const router = useRouter();

onMounted(() => {
  axios
    .get("http://localhost:8000/api/v1/memo/articles", {
      headers: {
        Authorization: `Bearer ${accessToken.value}`,
      },
    })
    // HACK: トークンrefresh処理は共通処理としてまとめる必要がある
    .then((response) => {
      articles.value = response.data;
      console.log(articles.value);
    })
    .catch((error) => {
      if (error.response?.status === 401) {
        // 401エラーが起きたとき、トークンrefresh
        axios
          .post("auth/jwt/refresh", {
            refresh: `${refreshToken.value}`,
          })
          .then((response) => {
            // storeのトークン更新
            store.refresh(response.data.access, response.data.refresh);
          })
          .catch(() => {
            // トークンrefresh出来なかったら、ログアウトしてログイン画面へ
            store.logout();
            router.push("/login");
          });
      }
    });
});
</script>

<template>
  <section class="alert alert-primary">
    <h1>タイムライン</h1>
    <div class="titles" v-for="article in articles" :key="article.id">
      <p id="title-timeline">"{{ article.title }}</p>
    </div>
  </section>
</template>

<style>
.titles {
  height: 50px;
  margin: 0;
  vertical-align: middle;
}

#title-timeline {
  height: 40px;
  border: 5px solid maroon;
  margin: 5px;
  background-color: #eee;
}
</style>
