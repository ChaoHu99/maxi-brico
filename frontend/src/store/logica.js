import _ from 'lodash'

export default {
    data:{
        cart: []
    },
    add(producto){
        var busqueda = _.find(this.data.cart, ['id',producto.id])
        if(typeof busqueda != 'object'){
            this.data.cart.push({
                barcode:producto.barcode,
                id:producto.id,
                nombre :producto.name,
                precio:producto.client_price,
                stock:producto.stock,
                cantidad: 1,
                image:producto.image,
                stripe_precio:producto.price
            })
        } 
    },
    inc(producto){
          var busqueda = _.find(this.data.cart, ['id',producto.id])
            //si está
          if(typeof busqueda == 'object'){
              //si está en el carrito dame el indice en la posición del array
            var index = _.indexOf(this.data.cart, busqueda)
            if(producto.stock>this.data.cart[index].cantidad){
                this.data.cart[index].cantidad++
            }
           }
    },
    dec(producto){
    var busqueda = _.find(this.data.cart, ['id',producto.id])
            //si está
          if(typeof busqueda == 'object'){
              //si está en el carrito dame el indice en la posición del array
            var index = _.indexOf(this.data.cart, busqueda)
            if(this.data.cart[index].cantidad==1){
                this.data.cart.splice(index, 1);
            }else{
                this.data.cart[index].cantidad--
            }
           }
    }
}