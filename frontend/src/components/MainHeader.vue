<template>
    <div class="container">
        <div class="header">
            <img class="logo" onClick="window.location.reload();" alt="MaxiBrico Logo" src="../assets/RedLogo.png"/>
            <div class="dropdown">
                
                <div class="dropdown__header" @click="toggleDropdown($event)">
                    <img class="user-icon" alt="MaxiBrico Logo" src="../assets/UserIcon.png"/>
                </div>
                
                <div class="dropdown__content">
                    <ul>
                        <li>Iniciar sesión</li>
                        <li>Regístrate</li>
                    </ul>
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
        padding-left: 5%;
        cursor: pointer;
        top: -10%;
        -ms-transform: translateY(10%);
        transform: translateY(10%);
    }
    
     .user-icon{
        float: right;
        position:fixed;
        top: 0%;
        right: 0%;
        width:50px;
        height: 50px;
        padding-right: 5%;
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
                    height: 20%;
                    width: 170px;
                    margin-right: 5%;
                    background: white;
                    opacity: 1;
                    visibility: visible;
                    color: black;
                    border-radius: 10px;
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