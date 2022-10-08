<template>
  <div id="mdeditor">
    <h1>Markdown Editor</h1>
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
#mdeditor {
  margin: 0;
  height: 100%;
}

#mdeditor,
h1 {
  font-size: 30px;
  padding: 5px;
}
</style>
