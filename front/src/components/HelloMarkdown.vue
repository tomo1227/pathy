<template>
  <div id="editor">
    <textarea :value="markdownText" @input="update"></textarea>
    <div class="preview" v-html="compiledMarkdown"></div>
  </div>
</template>

<script>
import * as DOMPurify from "dompurify";
import hljs from "highlight.js";
import "highlight.js/styles/base16/solarized-dark.css";
import { marked } from "marked";
import debounce from "lodash/debounce";

export default {
  name: "postForm",
  created: function () {
    marked.setOptions({
      langPrefix: "hljs language-",
      highlight: function (code, lang) {
        return hljs.highlightAuto(code, [lang]).value;
      },
    });
  },
  computed: {
    compiledMarkdown: function () {
      return DOMPurify.sanitize(marked(this.markdownText));
    },
  },
  methods: {
    update: debounce(function (e) {
      this.markdownText = e.target.value;
    }, 300),
  },
  data: function () {
    return {
      markdownText: "# Hello Markdown!!",
    };
  },
};
</script>

<style>
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
  font-size: 20px;
  font-family: "Monaco", courier, monospace;
  padding: 20px;
}

pre code.hljs {
  padding: 0.2em;
}

code {
  font-size: 18px;
  background-color: rgb(190, 190, 190);
  padding: 0.2em;
}
</style>
