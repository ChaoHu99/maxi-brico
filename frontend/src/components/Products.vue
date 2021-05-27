<template>
    <div>
      <table>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.name }}</td>
            <td>{{ product.description}}</td>   
          </tr>
        </tbody>
      </table>
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
        getProducts(){
            axios
            .get('http://127.0.0.1:8000/list/products/')
            .then( response => {
                this.products = response.data
            })
            .catch( e=> console.log(e))
        }
    }
    
}
</script>

<style>

</style>