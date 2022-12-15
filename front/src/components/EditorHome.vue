<script setup>
import * as DOMPurify from "dompurify";
import hljs from "highlight.js";
import "highlight.js/styles/base16/solarized-dark.css";
import { marked } from "marked";
import debounce from "lodash/debounce";
import { computed, ref } from "vue";
import { storeToRefs } from "pinia";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();
const { email } = storeToRefs(store);
const { accessToken } = storeToRefs(store);
const markdownTitle = ref("Title");
const markdownText = ref("# Hello Markdown!!");
const isPosted = ref(false);

// タイトル
const titlePreview = computed(() => {
  return markdownTitle.value;
});

const title = debounce((e) => {
  markdownTitle.value = e.target.value;
}, 100);

// 本文
marked.setOptions({
  langPrefix: "hljs language-",
  highlight: function (code, lang) {
    return hljs.highlightAuto(code, [lang]).value;
  },
});

const compiledMarkdown = computed(() => {
  return DOMPurify.sanitize(marked(markdownText.value));
});

const mdTextInput = debounce((e) => {
  markdownText.value = e.target.value;
}, 100);

const submit = () => {
  axios({
    method: "post",
    url: "memo/articles/",
    data: {
      user_email: email.value,
      title: markdownTitle.value,
      article_text: markdownText.value,
    },
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken.value}`,
    },
  })
    .then((response) => {
      // isPosted.value = true;
      console.log(response);
    })
    .catch((error) => {
      if (error.response?.status === 401) {
        store.refreshApi();
      }
    });
};
</script>

<template>
  <div id="post-btn-container">
    <button class="post-btn-item green-btn" @click="submit">投稿</button>
    <button class="post-btn-item yellow-btn">下書き</button>
    <button class="post-btn-item red-btn">削除</button>
  </div>
  <div id="post-status" v-show="isPosted">
    <p>投稿できました。</p>
  </div>
  <div id="editor-title">
    <div id="editor-title-input">
      <textarea
        id="title-textarea"
        :value="markdownTitle"
        @input="title"
      ></textarea>
    </div>
    <div id="editor-tilte-preview">
      <h1>{{ titlePreview }}</h1>
    </div>
  </div>
  <div id="editor">
    <textarea :value="markdownText" @input="mdTextInput"></textarea>
    <div class="preview" v-html="compiledMarkdown"></div>
  </div>
</template>

<style>
#post-btn-container {
  display: flex;
  height: 30px;
  justify-content: flex-end;
  padding: 0 15px;
}

@media screen and (max-width: 560px) {
  #post-btn-container {
    justify-content: center;
    padding: 0;
  }
}

#post-status {
  display: flex;
  height: 30px;
  justify-content: center;
  padding: 0 15px;
}

@media screen and (max-width: 560px) {
  #post-status {
    padding: 0;
  }
}

.post-btn-item {
  margin: 0 2px;
  width: 70px;
  box-shadow: 0 3px 5px rgb(0 0 0 / 50%);
  font-size: 14px;
  font-weight: bold;
}

@media screen and (max-width: 560px) {
  .post-btn-item {
    justify-content: center;
    width: 100%;
  }
}

.post-btn-item:hover {
  box-shadow: none;
  transform: scale(0.99, 0.99) translateY(2px);
}

.red-btn {
  border: 0;
  appearance: none;
  background-color: rgb(242 53 53 / 80%);
  border-radius: 5px;
}
.yellow-btn {
  border: 0;
  appearance: none;
  background-color: rgb(248 238 70);
  border-radius: 5px;
}
.green-btn {
  border: 0;
  appearance: none;
  background-color: rgb(17 247 109);
  border-radius: 5px;
}

#editor-title {
  display: flex;
  padding: 10px;
  height: 60px;
}

#editor-title-input {
  width: 50%;
}

#editor-tilte-preview {
  width: 50%;
}
#title-textarea {
  display: inline-block;
  width: 100%;
  height: 100%;
}

#editor {
  margin: 0;
  height: 70%;
  font-family: "Helvetica Neue", Arial, sans-serif;
  color: #333;
}

textarea,
#editor div {
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  padding: 0 20px;
}

textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 15px;
  font-family: "Monaco", courier, monospace;
  padding: 20px;
}

pre code.hljs {
  padding: 0.2em;
}

.preview {
  text-align: left;
}

.preview,
p,
h1,
h2,
h3,
h4 {
  padding: 0;
  margin: 0;
}

.preview,
p {
  font-size: 15px;
}

code {
  font-size: 15px;
  background-color: rgb(190, 190, 190);
  padding: 0.1em;
}
</style>
