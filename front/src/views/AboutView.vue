<template>
  <div class="about">
    <h1>This is an about page</h1>
    <HelloMarkdown />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloMarkdown from "@/components/HelloMarkdown.vue";

export default {
  name: "AboutView",
  components: {
    HelloMarkdown,
  },
};
</script>
