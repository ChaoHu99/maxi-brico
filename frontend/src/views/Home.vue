<template>
  <div id ="app">
    <div id = "header">
      <MainHeader></MainHeader>
    </div>
    <div id = "main-container">
      <ListProducts></ListProducts>
    </div>
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue'
import ListProducts from '@/components/ListProducts.vue'
export default {
  name: 'App',
  components: {
    MainHeader,
    ListProducts,
  }
}
</script>

<style scoped>
</style>
