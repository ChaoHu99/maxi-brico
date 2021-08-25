<template>
  <div id ="app">
    <div id = "header">
      <MainHeader></MainHeader>
    </div>
    <div id = "main-container">
      <div class="no-item" v-if="orders.length===0">NO TIENE PEDIDOS REGISTRADOS</div>
      <v-layout row wrap>
        <v-flex class="list" v-for="order in orders" :key="order.id">
          <v-card hover class="product-card">

            <v-card-title>
              <h3>{{ order.address}} {{order.creation_date.split('T')[0]}}</h3>
            </v-card-title>
            
            <v-card-text>
              Precio: {{order.price/100}} € <br>
              Estado: {{order.delivery_status}}
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue'
import axios from 'axios'
import store from '@/store.js'
export default {
  components: {
    MainHeader,
  },
  data(){
        return{
            orders:null
        }
    },
    mounted(){
        this.getOrders();
    },
    methods: {
        async getOrders(){
          let orders = await axios.get('http://127.0.0.1:8000/list/orders/'
          , {headers: { Authorization: `Bearer ${store.state.accessToken}`}}
          ).then( response => {
                this.orders = response.data
            })
          return orders;
        }
    }
}
</script>

<style scoped>

#main-container{
  margin-top: 100px;
}

.product-card{
  margin: 0 30px 20px 30px ;
  width: 450px;
}

.no-item{
  margin-top: 100px;
  text-align: center;
}

@media only screen and (max-width: 500px) {
  
.product-card{
  margin: 0 30px 20px 30px ;
  width: 300px;
}

}

</style>