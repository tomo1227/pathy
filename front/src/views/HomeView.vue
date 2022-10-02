<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld3 />
    <HelloWorld2 pipe1="これは最初のエリア" pipe2="次のエリア" />
    <HelloWorld msg="a" />
  </div>
</template>

<script>
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
