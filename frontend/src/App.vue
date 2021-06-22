<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <ListProducts></ListProducts>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import ListProducts from './components/ListProducts.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    ListProducts
  }
}
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
