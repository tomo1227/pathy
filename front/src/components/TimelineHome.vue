<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { storeToRefs } from "pinia";

const articles = ref([]);
const store = useAuthStore();
const { accessToken } = storeToRefs(store);

onMounted(() => {
  axios
    .get("memo/articles", {
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
        store.refreshApi();
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
  width: 100%;
  box-sizing: border-box;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
</style>
