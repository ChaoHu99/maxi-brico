<template>
  <div id ="app">
    <div id = "header">
      <MainHeader></MainHeader>
    </div>
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue'
export default {
  name: 'App',
  components: {
    MainHeader,
  }
}
</script>

<style scoped>
</style>