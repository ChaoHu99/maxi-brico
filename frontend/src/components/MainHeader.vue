<template>
    <header class="header">
    <div class="header">
        <router-link to="/"><img class="logo" alt="MaxiBrico Logo" src="../assets/RedLogo.png"/></router-link>
        <router-link to="/cart"><img class="cart-logo" alt="Cart Logo" src="../assets/CartLogo.png"/></router-link>
        <div class="dropdown">
            
            <div class="dropdown__header" @click="toggleDropdown($event)">
                <v-img class="user-icon" alt="MaxiBrico Logo" src="../assets/UserIcon.png"/>
            </div>
            
            <div class="dropdown__content">
                <router-link style="text-decoration: none; color: inherit;" to="/login">Iniciar sesión</router-link>
                <br><br>
                <router-link style="text-decoration: none; color: inherit;" to="/sign-up">Regístrate</router-link>
                <br><br>
                <router-link style="text-decoration: none; color: inherit;" to="/logout">Cierra sesión</router-link>                
            </div>
        </div>
    </div>
    </header>
    
</template>

<script>
    export default {
        methods: {
            toggleDropdown (event) {
                event.currentTarget.classList.toggle('is-active')
            }
        }
    }
</script>

<style lang="scss" scoped>

    .header{
        background-color: black;
        top: 0%;
        left: 0%;
        right: 0%;
        height: 60px;
        position: absolute;
    }

    .logo{
        width:50px;
        height: 50px;
        margin-left: 5%;
        top: 0%;
        -ms-transform: translateY(10%);
        transform: translateY(10%);
    }

    .cart-logo{
        position: absolute;
        float: right;
        top: 0%;
        margin-right: 50px;
        right: 10%;
        width:50px;
        height: 50px;
        cursor: pointer;
        -ms-transform: translateY(10%);
        transform: translateY(10%);
    }
    
     .user-icon{
        position: absolute;
        float: right;
        top: 0%;
        right: 5%;
        margin-left: 50px;
        width:50px;
        height: 50px;
        cursor: pointer;
        -ms-transform: translateY(10%);
        transform: translateY(10%);
    }

    .dropdown {
        &__header {            
            &.is-active {                
                + .dropdown__content {
                    float: right;
                    border-style: groove;
                    border-width: thin;
                    height: 120px;
                    width: 150px;
                    margin-right: 5%;
                    padding-top: 10px;
                    padding-left: 30px;
                    background: white;
                    opacity: 1;
                    visibility: visible;
                    color: black;
                    border-radius: 5px;
                    z-index: 1;
                    position: relative;
                }
            }
        }
        &__content {
            height: 0;
            opacity: 0;
            overflow: hidden;
            transition: opacity .3s;
            visibility: hidden;
        }
    }

</style>