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

export default {
  setup() {
    const data = reactive({
      word: "This is axios sample.",
      title: "",
      article_text: "",
    });
    const token =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1Mzg4NTg0LCJqdGkiOiI0ODFjNzBjYmQ0OTI0YTFiYmIxZGFiMDJiYjk4NjQyOSIsInVzZXJfaWQiOjF9.FiGR5FoTXRxLMlrHcVQFXBxj5XebB4H7fmg6gfg8odQ";

    const getData = async () => {
      let result = await axios.get("memo/articles/1/", {
        headers: {
          Authorization: `JWT ${token}`,
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
