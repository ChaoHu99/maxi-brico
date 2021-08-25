<template>
  <div>
    <div>
      <MainHeader></MainHeader>
    </div>
    <h1>Inicia sesión en MaxiBrico</h1>
    <p class="incorrect" v-if="incorrectAuth">Credenciales incorrectas, por favor prueba de nuevo</p>
    <form class="form" v-on:submit.prevent="login">
      <div class="form-group">
        <input type="email" name="username" id="user" v-model="username" class="form-control" placeholder="Correo electrónico">
      </div>
      <div class="form-group">
        <input type="password" name="password" id="pass" v-model="password" class="form-control" placeholder="Contraseña">
      </div>
      <div class="final">
        <button type="submit" class="btn">Inicia sesión</button><br>
        <router-link class="register" to="/sign-up">Si no tiene cuenta puede registrarse aquí</router-link>
      </div>
    </form>      
  </div>
</template>

<script>
import store from '@/store.js'
import MainHeader from '@/components/MainHeader.vue'
export default {
    components: {
      MainHeader,
    },
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        incorrectAuth: false
      }
    },
    methods: {
      login () { 
        store.dispatch('userLogin', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
        }
      }
  }
</script>

<style scoped>

h1{
    margin-top: 120px;
    text-align: center;
  }

.incorrect{
  margin-top:50px;
  text-align: center;
}

.form{
    margin: 30px 20% 0 20%;
    border-style: solid;
    border-color: #ddd ;
    width: 60%;
    
  }

  .btn{
    background-color: rgb(216, 54, 54);
    border-radius: 5px;
    color: rgb(0, 0, 0);
    height: 40px;
    width: 150px;

}

.form-control{
  width: 100%; 
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

.final{
  text-align: center;
}

</style>