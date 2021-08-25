<template>
  <div id ="app">
    <div id = "header">
      <MainHeader></MainHeader>
      <h1>Regístrate en MaxiBrico</h1>
    </div>
      <div class="sign-up">
        <form @submit.prevent="signup">
          <div>
            <label class="label" for="username">Correo electrónico</label><br>
            <input class="input" id="username" v-model="username" placeholder="Correo electrónico" type="email">
          </div>
          <div>
            <label class="label" for="name">Nombre</label><br>
            <input class="input" id="name" v-model="name" placeholder="Nombre" type="text">
          </div>
          <div>
            <label class="label" for="surname">Apellidos</label><br>
            <input class="input" id="surname" v-model="surname" placeholder="Apellidos" type="text">
          </div>
          <div>
            <label class="label" for="phone">Teléfono</label><br>
            <input class="input" id="phone" v-model="phone" placeholder="Teléfono" type="number">
          </div>
          <div>
            <label class="label" for="password">Contraseña</label><br>
            <input class="input" id="password" v-model="password" placeholder="Contraseña" type="password">
          </div>
          <div class="checkbox">
            <input type="checkbox" required> He leido y acepto los <router-link to="/terms">términos y condiciones</router-link>
          </div>
          <div class="final">
            <button @click="validation" class="btn" type="submit"> Regístrate </button>
            <p id ="restriction"></p>
          </div>
        </form>
      </div> 
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue'
export default {
  name: 'App',
  data() {
    return {
      username: "",
      name: "",
      surname: "",
      phone: "",
      password: "",
    };
  },
  methods: {
      validation() {
        let a = document.getElementById("username").value;
        let b = document.getElementById("name").value;
        let c = document.getElementById("surname").value;
        let d = document.getElementById("phone").value;
        let e = document.getElementById("password").value;
        let text;
        if (a == "" || b == "" || c == "" || d == "" || e == "") {
          text = "Debe rellenar todos los campos";
          document.getElementById("restriction").innerHTML = text;
        }
        else if (d.toString().length != 9){
          text = "El teléfono debe tener 9 dígitos";
          document.getElementById("restriction").innerHTML = text;
        } else {
          text = "Usuario creado";
          document.getElementById("restriction").innerHTML = text;
        }
      },
    async signup() {
      const { username, name, surname, phone, password} = this;
      const res = await fetch('http://localhost:8000/create/user/',
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username,
            name,
            surname,
            phone,
            password
          })
        }
      );
      const data = await res.json();
      console.log(data);
    }
  },
  components: {
    MainHeader,
  }
}
</script>

<style scoped>

  .checkbox{
    text-align: center;
    margin-bottom: 10px;
  }

  .sign-up{
    margin: 30px 10% 0 10%;
    border-style: solid;
    border-color: #ddd ;
    width: 80%;
    
  }
  .input {
  width: 100%; 
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
  }
  h1{
    margin-top: 80px;
    text-align: center;
  }
  .label{
    padding-left: 15px;
  }

  .btn{
    background-color: rgb(216, 54, 54);
    border-radius: 5px;
    color: rgb(0, 0, 0);
    height: 40px;
    width: 150px;

}

#restriction{
  margin:10px 0 10px 0;
}

.final{
  text-align: center;
}

</style>