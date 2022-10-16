<template>
  <div class="home">
    <HelloWorld3 />
    <HelloWorld2 pipe1="これは最初のエリア" pipe2="次のエリア" />
    <HelloWorld msg="a" />
  </div>
</template>

<script>
// HACK: setup scirptで書き直す必要あり
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import HelloWorld2 from "@/components/HelloWorld2.vue";
import HelloWorld3 from "@/components/HelloWorld3.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld3,
    HelloWorld2,
    HelloWorld,
  },
};
</script>

<style>
.img {
  width: 30px;
  height: 5px;
}
</style>
