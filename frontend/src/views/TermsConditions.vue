<template>
    <div>
        <div>
            <MainHeader></MainHeader>
        </div>
        <div id="container">
            <h1>Términos y condiciones</h1><br>
            <div class="contenido">
                <h2> 1. Descripción </h2><br>
                <p>Los términos y condiciones tienen por objetivo regular el acceso y los términos de uso de la
                Plataforma. Se ruega leer atentamente estas Condiciones Generales de Uso para un mejor conocimiento de la plataforma.</p><br>
                <h2>2. Registro en la plataforma y creación de una cuenta</h2><br>
                <p>Al crear tu cuenta, el usuario se compromete a proporcionar información
                    verídica y precisa, con el objetivo de garantizar su relevancia y precisión durante la relación contractual con MaxiBrico.
                    La plataforma utilizará la información proporcionada por el usuario para fines comerciales entre 
                    la entidad y el cliente. </p><br>
                <p>En caso de que te registres, te comprometes a guardar en secreto la
			contraseña seleccionada durante la creación de la cuenta y a no comunicársela a ninguna otra persona. En
			caso de pérdida o divulgación. Tú eres el único responsable del uso de tu cuenta por parte de terceras partes</p><br>
                <p>MaxiBrico puede que verifique la información proporcionada para la prevención de fraude.</p><br>
                <h2>2. Compras de productos</h2><br>
                <p>En el momento del pedido, el pasajero realizará el pago en línea por la
			cantidad de costes especificados. Una vez recibido el pago por parte de MaxiBrico, el cliente puede encontrar
			su reserva con los datos correspondientes en el apartado "Mis pedidos".</p><br>
                <p>La tarjeta empleada para la compra deberá ser de su propiedad o de un conocido, MaxiBrico no se hace cargo de malos usos de tarjetas en la plataforma.</p><br>
                <h2>3. Manejo de datos personales.</h2><br>
                <p>Con el uso de la plataforma por tu parte, MaxiBrico recopilará y procesará tu información personal.
			Al utilizar la plataforma y registrarte como usuario, reconoces y aceptas el procesamiento de tus datos
			personales por parte de MaxiBrico con conformidad con la legislación aplicable</p><br>
                

                

            </div>

        </div>
    </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue'
export default {
    components: {
      MainHeader,
    }
}
</script>

<style scoped>

#container{
    margin-top: 100px;
}
h1{
    text-align: center;
}

.contenido{
    margin: 30px 10% 50px 10%;
    border-style: solid;
    border-color: #ddd ;
    width: 80%;
}

</style>