<template>
  <div class="logout">
  </div>
</template>

<script>
import store from '@/store.js'
export default {
    created () {
      store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
    }
  }
</script>