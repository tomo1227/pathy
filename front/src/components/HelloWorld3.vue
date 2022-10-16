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
// HACK: setup scirptで書き直す必要あり
import axios from "axios";
import { reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
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
    const { refreshToken } = storeToRefs(store);
    const router = useRouter();

    const getData = async () => {
      await axios
        .get("auth/users/me/", {
          headers: {
            Authorization: `Bearer ${accessToken.value}`,
          },
        })
        .then((response) => {
          data.title = response.data.username;
          data.article_text = response.data.email;
        })
        .catch((error) => {
          if (error.response?.status === 401) {
            axios
              .post("auth/jwt/refresh", {
                refresh: `${refreshToken.value}`,
              })
              .then((response) => {
                store.refresh(response.data.access, response.data.refresh);
                console.log(accessToken.value);
              })
              .catch(() => {
                store.logout();
                router.push("/login");
              });
          }
        });
    };
    onMounted(() => {
      getData();
    });
    return { data, getData };
  },
};
</script>
