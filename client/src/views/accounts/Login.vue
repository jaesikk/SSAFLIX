<template>
  <div class="w-50">
    <h1>로그인</h1>
  <form>
  <div class="mb-3">
    <label for="username" class="form-label">Username</label>
    <input type="text" class="form-control" id="username" v-model="credentials.username">
    <div id="emailHelp" class="form-text">We'll never share your information with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="password" class="form-label">Password</label>
    <input
      type="password"
      class="form-control"
      id="password"
      v-model="credentials.password"
      @keyup.enter="login"
    >
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="button" class="btn btn-outline-primary" @click="login">로그인</button>
  </form>

  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: this.credentials,
      }).then((res) => {
        localStorage.setItem('jwt', res.data.token)
        console.log(res)
        this.$emit('login')
        this.$router.push({ name: 'Home' }) 
        // App에게 login 전달
      })
    }
  },
}
</script>

<style>

</style>