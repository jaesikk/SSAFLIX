<template>
<div id="back">
  <img id="img" src="https://an2-img.amz.wtchn.net/image/v2/27a141759f10a71e73a27ecef9ac4634.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKaVlXTnJaM0p2ZFc1a0lqcDdJbklpT2pJMU5Td2laeUk2TWpVMUxDSmlJam95TlRWOUxDSndZWFJvSWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk1EZzNNVFkzTVRNMU1EVTFORGN5TURraWZRLjlINVo2cDFMOVpCTUM1R2huT010TmVraldTRzk1YnBfTkk4U3lzQXRmREE" alt="">
  <div id="login">

    <h1>로그인</h1>
    <hr>
    <form>
    <div>
      <label for="username" class="form-label">Username</label>
      <input type="text" class="form-control" id="username" v-model="credentials.username">
    </div>
    <br>
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
        <router-link :to="{ name: 'Signup' }" class="nav-link">아직 회원이 아니신가요?</router-link>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

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
    // login: function () {
    //   axios({
    //     method: 'POST',
    //     url: SERVER_URL + '/accounts/api-token-auth/',
    //     data: this.credentials,
    //   }).then((res) => {
    //     console.log(res.data.userId)
    //     localStorage.setItem('jwt', res.data.token)
    //     this.$emit('login')
    //     // App에게 login 전달
    //   })
    // }
    login: function () {
      this.$store.dispatch('userStore/loginUser', this.credentials)
      // axios.defaults.headers.common['Authorization'] = `JWT ${this.$store.state.token}`
      this.$emit('login')
      this.$router.push({ name: 'Home' }) 
    }
  },
}
</script>

<style>
#login {
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -50%);
}
/* 배경이미지를 넣고 싶을때 backgrond-image로 스타일링 하는것보다
img요소를 넣고 그 요소를 스타일링하는것이 더 간편*/
#img {
  height: 100%;
  width: 100%;
  opacity: 0.3;
  position: fixed;
  top: 0px;
  bottom: 0px;
  left: 0px;
  right: 0px;
}
</style>