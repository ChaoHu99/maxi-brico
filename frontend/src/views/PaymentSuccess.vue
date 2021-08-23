<template>
    <div>
        <MainHeader></MainHeader>
        <div id = "main-container">
            <v-img 
                height="100px"
                width="300px" 
                alt="Ahorra Panel" src="../assets/Ahorra.png"/><br><br>
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
    margin-top:150px;
    margin-left: 10%;
}
    
</style>