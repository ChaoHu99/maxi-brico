<template>
  <div id ="app">
    <div id = "header">
      <MainHeader></MainHeader>
      <h2>Regístrate en MaxiBrico</h2>
      <div class="sign-up">
        <form @submit.prevent="login">
          <div>
            <label class="label" for="username">Correo electrónico</label><br>
            <input name="username" v-model="username" placeholder="Correo electrónico" type="email">
          </div>
          <div>
            <label class="label" for="name">Nombre</label><br>
            <input name="name" v-model="name" placeholder="Nombre" type="text">
          </div>
          <div>
            <label class="label" for="surname">Apellidos</label><br>
            <input name="surname" v-model="surname" placeholder="Apellidos" type="text">
          </div>
          <div>
            <label class="label" for="phone">Teléfono</label><br>
            <input name="phone" v-model="phone" placeholder="Teléfono" type="text">
          </div>
          <div>
            <label class="label" for="password">Contraseña</label><br>
            <input name="password" v-model="password" placeholder="Contraseña" type="password">
          </div>
          <input type="submit" value="register">
        </form>
      </div>
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
    async login() {
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

  .sign-up{
    margin: 30px 10% 0 10%;
    border-style: solid;
    border-color: #ddd ;
    width: 80%;
    
  }
  input[type=text], input[type=password], input[type=email] {
  width: 100%; 
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
  }
  h2{
    margin-top: 80px;
    text-align: center;
  }
  .label{
    padding-left: 15px;
  }

</style>