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
          Stock: {{product.stock}}<br>
          Color: {{product.colour}}<br>
          Medida: {{product.size}}
        </v-card-text>

        <v-card-actions>
          <v-btn class="add-cart" @click.native="addCurrentProductToCart(product)">Add to Cart</v-btn>
        </v-card-actions>
        </div>  
    </v-card>
    
  </div>
</template>

<script>
// import { mapActions } from 'vuex';
import axios from 'axios'
export default {
    data(){
        return{
            product: {}
        }
    },
    mounted(){
        this.getProduct();
    },
    methods: {
        async getProduct(){
          let barcode = this.$route.params.barcode
          let product = await axios.get('http://127.0.0.1:8000/list/product/'+barcode).then( response => {
                this.product = response.data
            })
          return product;
        },
        addProductToCart(product) {
          this.addProduct(product);
        },
        addCurrentProduct(product) {
          this.currentProduct(product);
        },
    }
    
}
</script>

<style scoped>

.product-card{
    top: 100px;
    margin-left:10%;
    margin-right: 10%;
    height: 550px; 
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
    transform: translateY(-110%);
    float: right;
    margin-right: 20%;
  }
}

</style>