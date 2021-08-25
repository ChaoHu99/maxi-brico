<template>
  <div>
    <v-container>
      <v-layout row wrap>
        <v-flex class="list" v-for="product in products" :key="product.id">
          <router-link style="text-decoration: none;" :to="{path: '/product/' + product.barcode}" >
          <v-card hover class="product-card">
            <v-img
              :src=product.image
              height="200px"
            >
            </v-img>

            <v-card-title>
              <h3>{{ product.name}}</h3>
            </v-card-title>
            
            <v-card-text>
              Precio: {{product.client_price}} € <br>
              Stock: {{product.stock}}
            </v-card-text>
          </v-card>
          </router-link>
        </v-flex>
      </v-layout>
    </v-container>  
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            products:null
        }
    },
    mounted(){
        this.getProducts();
    },
    methods: {
        async getProducts(){
          let products = await axios.get('http://127.0.0.1:8000/list/products/'
          // , {headers: { Authorization: `Bearer ${store.state.accessToken}`}}
          ).then( response => {
                this.products = response.data
            })
          return products;
        }
    }
    
}
</script>

<style scoped>
  .list{
    margin-top: 80px;

  }
  .product-card{
    width: 200px;
    margin-left:2%;
  }

</style> 