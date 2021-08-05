<template>
    <div class="container">
        <div class="header">
            <v-img class="logo" onClick="window.location.reload();" alt="MaxiBrico Logo" src="../assets/RedLogo.png"/>
            <div class="dropdown">
                
                <div class="dropdown__header" @click="toggleDropdown($event)">
                    <v-img class="user-icon" alt="MaxiBrico Logo" src="../assets/UserIcon.png"/>
                </div>
                
                <div class="dropdown__content">
                    <button type="button" >Iniciar sesión</button>
                    <br><br>
                    <button type="button" >Regístrate</button>
                    
                </div>
            </div>
        </div>
    </div>
    
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
        width: 100%;
        height: 60px;
        position: absolute;
        display: inline;
    }

    .logo{
        width:50px;
        height: 50px;
        left: 5%;
        cursor: pointer;
        top: 0%;
        -ms-transform: translateY(10%);
        transform: translateY(10%);
    }
    
     .user-icon{
        position: absolute;
        float: right;
        top: 0%;
        right: 5%;
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
                    height: 80px;
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