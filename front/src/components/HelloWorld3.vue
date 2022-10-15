<template>
  <section class="alert alert-primary">
    <h1>{{ data.word }}</h1>
    <p>{{ data.title }}</p>
    <textarea
      v-model="data.article_text"
      rows="5"
      class="form-control"
    ></textarea>
  </section>
</template>

<script>
import axios from "axios";
import { reactive, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { storeToRefs } from "pinia";

export default {
  setup() {
    const data = reactive({
      word: "This is axios sample.",
      title: "",
      article_text: "",
    });
    const store = useAuthStore();
    const { accessToken } = storeToRefs(store);

    const getData = async () => {
      let result = await axios.get("auth/users/me/", {
        headers: {
          Authorization: `Bearer ${accessToken.value}`,
        },
      });
      data.title = result.data.title;
      data.article_text = result.data.article_text;
    };
    onMounted(() => {
      getData();
    });
    return { data, getData };
  },
};
</script>
