<template>
  <div class="edit">
    <h1>Hello Markdown Editor</h1>
    <HelloMarkdown />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloMarkdown from "@/components/HelloMarkdown.vue";

export default {
  name: "EditView",
  components: {
    HelloMarkdown,
  },
};
</script>

<style>
div {
  margin: 0;
  height: 100%;
}

#edit {
  margin: 0;
  height: 100%;
}
</style>
