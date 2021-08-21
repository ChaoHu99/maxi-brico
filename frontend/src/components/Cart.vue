<template>
    <div class="todo">
        <MainHeader class="header"></MainHeader>
        <div class="no-item" v-if="tam===0">NO TIENE PRODUCTOS EN EL CARRITO</div>
          <div class="car_pro" v-for="item in items" :key="item.id">
            <div class="cuerpo">
                <v-img class="image"
                    :src=item.image
                    height="100px"
                    width="100px"
                >
                </v-img>
                <div class="feature">{{item.nombre}} </div>
                    <br>
                 <div class="feature">Cantidad: {{item.cantidad}}</div>
                    <br>
                 <div class="feature">Precio unidad: {{item.precio}}€</div>
            </div>
            <div class="precio"> Precio: {{item.cantidad * item.precio}} €</div>
          </div>

        <div v-if="tam>0" class="total">
            <div>
                <p>Precio total: {{total}}€</p><br>
            </div>
            <button class="btn"> Tramitar pedido </button>
        </div>

    </div>
</template>
<script>
import logica from '@/store/logica.js'
import _ from 'lodash'
import MainHeader from '../components/MainHeader.vue'
    export default {
        components:{
        MainHeader
    },
        data(){
            return {
              items: logica.data.cart,
              tam: logica.data.cart.length
            }
        },
        computed: {
           total(){
               return _.sumBy(this.items, function(it) {
                   return  (it.precio * it.cantidad)
                })
            }
        }
    }
</script>
<style>

.car_pro {
    display:flex;
    justify-content: space-between;
    padding: .8em;
    background-color: #fff;
    box-shadow: 0 0 10px gray;
    margin-top: 3.8em;
    height: 130px;
}
.total{
    border: 1px solid black;
     padding: .5em;
    text-align: center;
}
.feature{
    margin-left: 300px;
    transform: translateY(-500%);
}
.image{
    margin-left: 100px;
}
.no-item{
    margin-top: 300px;
    text-align: center;
}
.precio{
    margin-right: 100px;
    margin-top:35px;
    border: 1px solid black;
    padding-top: 10px;
    height: 40px;
    width: 80px;
    text-align:center;
    border-radius: 5px;
}

.btn{
    background-color: red;
    border-radius: 5px;
    color: rgb(0, 0, 0);
    height: 40px;
    width: 150px;

}

@media only screen and (max-width: 700px) {

.image{
    margin-left: 5%;
}

.feature{
    margin-left: 50%;
    transform: translateY(-500%);
    width:200px;
}
.precio{
    margin-right: 2%;
    margin-top:35px;
    border: 1px solid black;
    padding-top: 10px;
    height: 40px;
    width: 80px;
    text-align:center;
    border-radius: 5px;
}

}
  
</style>