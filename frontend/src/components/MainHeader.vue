<template>
    <div class="header">
        <img class="logo" onClick="window.location.reload();" alt="MaxiBrico Logo" src="../assets/RedLogo.png">
        <button class="sign-up" type="button" onclick="alert('Sign up!')">Regístrate</button>
        <button class="sign-in" type="button" onclick="alert('Sign in!')">Iniciar sesión</button>
        
    </div>
</template>

<script>

</script>

<style scoped>
    .header{
        background: rgb(0, 0, 0);
        top: 0%;
        left: 0%;
        width: 100%;
        position: absolute;
        
    }

    .logo{
        margin: auto;
        width:50px;
        height: 50px;
        padding: 0.4% 0.4% 0.1% 5%;
        cursor: pointer;
    }

    .sign-in{
        float: right;
        background-color: rgb(224, 43, 43);
        border: none;
        color: white;
        width:8%;
        height: 30px;
        margin: 1% 0% 0.1% 0.4%;
        cursor: pointer;

    }
    .sign-up{
        float: right;
        background-color: black;
        border: none;
        color: white;
        width:8%;
        height: 30px;
        text-align: center;
        margin: 1% 3% 0.1% 0.4%;
        cursor: pointer;
    }

    @media only screen and (max-width: 1200px) {
        .sign-in{
            float: right;
            background-color: rgb(224, 43, 43);
            border: none;
            color: white;
            width:12%;
            height: 40px;
            margin: 1% 0% 0.1% 0.4%;
            cursor: pointer;

        }
        .sign-up{
            float: right;
            background-color: black;
            border: none;
            color: white;
            width:9%;
            height: 40px;
            text-align: center;
            margin: 1% 8% 0.1% 0.4%;
            cursor: pointer;
        }
    }

     @media only screen and (max-width: 480px) {
        .logo{
        margin: auto;
        width:50px;
        height: 50px;
        padding: 0.8% 0.4% 0.1% 5%;
        cursor: pointer;
    }
        
        .sign-in{
            float: right;
            background-color: rgb(224, 43, 43);
            border: none;
            color: white;
            width:18%;
            height: 40px;
            margin: 2% 0% 0.1% 0.4%;
            cursor: pointer;
            font-size: 12px;
        }
        .sign-up{
            float: right;
            background-color: black;
            border: none;
            color: white;
            width:14%;
            height: 40px;
            text-align: center;
            margin: 2% 8% 0.1% 0.4%;
            cursor: pointer;
            font-size: 12px;
        }
    }

</style>