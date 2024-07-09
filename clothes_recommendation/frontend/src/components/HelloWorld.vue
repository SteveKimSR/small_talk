<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="goToInputComponent">Go to Input Component</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello, Vue!'
    };
  },
  methods: {
    goToInputComponent() {
      this.$emit('change-view', 'InputComponent');
    }
  }
};
</script>

<style scoped>
h1 {
  color: #42b983;
}
button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
}
</style>
