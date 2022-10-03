<template>
  <div>
    <div class="area1">{{ pipe1 }}</div>
    <div class="area2">{{ pipe2 }}</div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld2",
  props: {
    pipe1: String,
    pipe2: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.area1 {
  border: 3px #000000 solid;
}
.area2 {
  border: 3px #ff0000 solid;
}
</style>
