<template>
  <div id="app">
    <MainHeader></MainHeader>
    <ListProducts></ListProducts>
  </div>
</template>

<script>
import MainHeader from './components/MainHeader.vue'
import ListProducts from './components/ListProducts.vue'

export default {
  name: 'App',
  components: {
    MainHeader,
    ListProducts
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
