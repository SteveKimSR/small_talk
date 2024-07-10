<template>
  <div id="app">
    <component :is="currentView" @change-view="changeView" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import InputComponent from './components/InputComponent.vue';
import PictureOut from './components/PictureOut.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    InputComponent,
    PictureOut
  },
  data() {
    return {
      currentView: 'HelloWorld'
    };
  },
  methods: {
    changeView(view) {
      this.currentView = view;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
