<template>
    <div>
        <MainHeader></MainHeader>
        <div id = "main-container">
            <Product></Product>
        </div>
    </div>
</template>

<script>
import Product from '../components/Product.vue'
import MainHeader from '../components/MainHeader.vue'
export default {
    components:{
        Product,
        MainHeader
    }
}
</script>

<style scoped>

    
</style>