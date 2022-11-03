<template>
  <div id="mdeditor">
    <!-- <h1>Markdown Editor</h1> -->
    <EditorHome />
  </div>
</template>

<script>
// HACK: setup scirptで書き直す必要あり
import EditorHome from "@/components/EditorHome.vue";

export default {
  name: "EditView",
  components: {
    EditorHome,
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
  padding: 2px;
}
</style>
