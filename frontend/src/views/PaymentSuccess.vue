<template>
    <div>
        <MainHeader></MainHeader>
        <div id = "main-container">
            <h1>¡Se ha realizado el pago correctamente!</h1><br>
            <h2>Muchas gracias por su compra.</h2>                        
        </div>
    </div>
</template>

<script>
import MainHeader from '../components/MainHeader.vue'
export default {
    components:{
        MainHeader
    }
}
</script>

<style scoped>
#main-container{
    margin-top:100px;
    margin-left: 10%;
}
    
</style>