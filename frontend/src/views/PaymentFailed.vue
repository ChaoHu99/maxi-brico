<template>
    <div>
        <MainHeader></MainHeader>
        <div id = "main-container">
            <h1>¡Ha ocurrido un problema durante el pago!</h1><br>
            <h2>Prueba a tramitar el pedido de nuevo.</h2><br>
            <h3>¡Asegúrate de que toda la información sea correcta!</h3>   
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