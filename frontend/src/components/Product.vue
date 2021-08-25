<template>
  <div class="product">
    <v-card class="product-card">
      
      
      <v-img
        :src=product.image
        height="300px"
        width="300px"
      >
      </v-img>
      
      <div class="features">
        <v-card-title>
          <h3>{{ product.name}}</h3>
        </v-card-title>
        
        <v-card-text>
          {{product.description}}<br>
          Precio: {{product.client_price}} € <br>
          Color: {{product.colour}}<br>
          Medida: {{product.size}}
        </v-card-text>

        <v-card-actions>
          <v-btn class="add-cart" v-if="qtyCart===0 && product.stock>0" @click="addToCart">Add to Cart</v-btn>
            <div class="botones" v-else>
              <v-btn class="btns" @click="inc">+</v-btn>
              <span class="qty" v-if="qtyCart>0">  x {{qtyCart}}  </span>
              <v-btn class="btns" @click="dec"> - </v-btn>
          <div v-if="qtyCart==product.stock" class="restriction">No hay más depósito</div>
          </div>
        </v-card-actions>
        </div>  
    </v-card>
    
  </div>
</template>

<script>
// import { mapActions } from 'vuex';
import _ from 'lodash'
import logica from '@/store/logica.js'
import axios from 'axios'
export default {
  props:['producto'],
    data(){
        return{
            product: {},
            shared:logica.data
        }
    },
    mounted(){
        this.getProduct();
    },
    computed: {
        qtyCart(){
            var busqueda = _.find(this.shared.cart, ['id',this.product.id])
            if(typeof busqueda == 'object'){
               return busqueda.cantidad
            }else{
              return 0;
            }
        }
    },
    methods: {
        async getProduct(){
          let barcode = this.$route.params.barcode
          let product = await axios.get('http://127.0.0.1:8000/product/'+barcode).then( response => {
                this.product = response.data
            })
          return product;
        },
        addToCart(){            
            logica.add(this.product)
        },
        inc(){
            logica.inc(this.product)
        },
        dec(){
            logica.dec(this.product)
        }
    }
    
}
</script>

<style scoped>

.product-card{
    top: 100px;
    margin-left:10%;
    margin-right: 10%;
    height: 580px; 
  }

.restriction{
  padding-top: 10px;
  color: red;
}

@media only screen and (max-width: 700px) {

  .product-card{
    max-width: 300px;
  }

}


@media only screen and (min-width: 700px) {

  .product-card{
    top: 100px;
    margin-left:10%;
    margin-right: 10%;
    padding-top: 25px;
    height: 380px;
  }

    .features{
    position: static;
    transform: translateY(-100%);
    float: right;
    margin-right: 20%;
  }
}

</style>