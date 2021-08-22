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
            <div class="precio"> Precio: {{item.cantidad * item.stripe_precio/100}} €</div>
          </div>

        <div v-if="tam>0" class="total">
            <div>
                <p>Precio total: {{total}}€</p><br>
            </div>
            <div class="dropdown">
                <div class="dropdown__header" @click="toggleDropdown($event)">
                    <button class="btn"> Tramitar pedido </button>
                </div>
                
                <div class="dropdown__content">
                    <input class="address" name="address" v-model="address" placeholder="Introduzca su dirección" type="text"><br>
                    <button @click="pay" class="btn"> Pagar ahora </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script src="https://js.stripe.com/v3/"></script>
<script>
import logica from '@/store/logica.js'
import _ from 'lodash'
import MainHeader from '../components/MainHeader.vue'
import axios from 'axios'
export default {
    components:{
    MainHeader
},
    data(){
        return {
          items: logica.data.cart,
          tam: logica.data.cart.length,
          pub_key: '',
          stripe: null,
          address: "",
          order:{}
        }
    },
    async mounted(){
        await this.getPubKey()
        this.stripe = Stripe(this.pub_key)
    },
    computed: {
       total(){
           return _.sumBy(this.items, function(it) {
               return  (it.stripe_precio * it.cantidad)/100
            })
        }
    },
    methods: {
        async getPubKey() {
            await axios.get('http://127.0.0.1:8000/stripe/get-stripe-pub-key/').then( response => {
                this.pub_key = response.data.pub_key
            })
        },
        async pay() {
            const products = this.items.map((item) => item.id);
            let aux = _.sumBy(this.items, function(it) {
               return  (it.stripe_precio * it.cantidad)
            });
            const price = aux;
            const { user, address} = this;
            let res = await fetch('http://localhost:8000/create/order/',
                {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    user,
                    products,
                    price,
                    address,
                })
            })
            res = await res.json()
            this.order = res.order
            const data = {
                order: this.order
            }
            axios
                .post('http://127.0.0.1:8000/stripe/create-checkout-session/', data)
                .then(response => {
                    return this.stripe.redirectToCheckout({sessionId: response.data.sessionId})
                })
                .catch(error => {
                    console.log('Error:', error)
                })
            },
        toggleDropdown (event) {
            event.currentTarget.classList.toggle('is-active')
        }
    }
}
</script>
<style lang="scss">

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
    width: 120px;
    text-align:center;
    border-radius: 5px;
}

.btn{
    background-color: rgb(216, 54, 54);
    border-radius: 5px;
    color: rgb(0, 0, 0);
    height: 40px;
    width: 150px;

}
.dropdown {
        &__header {            
            &.is-active {                
                + .dropdown__content {
                    border-style: groove;
                    border-width: thin;
                    height: 100px;
                    width: 500px;
                    margin-top:10px;
                    background: white;
                    opacity: 1;
                    visibility: visible;
                    color: black;
                    border-radius: 5px;
                    z-index: 1;
                    position: relative;
                    display: inline-block;
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
.address{
    text-align: center;
    margin-top: 10px;
    height: 30px;
    width: 70%;
    margin-bottom: 10px;
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
    width: 120px;
    text-align:center;
    border-radius: 5px;
}
.dropdown {
        &__header {            
            &.is-active {                
                + .dropdown__content {
                    width: 80%;
                }
            }
        }
    }

}
  
</style>