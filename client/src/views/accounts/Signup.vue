<template>
  <div class="w-50">
    <h1>회원가입</h1>
    <div class="mb-3">
      <label for="username" class="form-label">Username</label>
      <input
        type="text"
        class="form-control"
        id="username"
        v-model="credentials.username"
        @input="changedid"
      >
      <button class="btn btn-outline-primary" @click="id_check">중복확인</button>
      <div id="emailHelp" class="form-text">We'll never share your information with anyone else.</div>
    </div>

    <div class="mb-3">
      <label for="password" class="form-label">Password</label>
      <input
        type="password"
        class="form-control"
        id="password"
        v-model="credentials.password"
      >
    </div>
    <div class="mb-3">
      <label for="passwordConfirmation" class="form-label">Password confirm</label>
      <input
        type="password"
        class="form-control"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
      >
    </div>
    <button type="button" class="btn btn-outline-primary" @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
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
        passwordConfirmation: '',
        idCheck: false,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/signup/',
        data: this.credentials,
      }).then((res) => {
        console.log(res)
        this.$router.push({ name: 'Login' })
        // 회원가입 후 로그인 페이지로
      }).catch((err) => {
        console.log(err.response.data.error)
        alert(err.response.data.error)
      })
    },
    // 중복 ID를 체크하는 함수
    id_check: function () {
      // username이 있다면
      if (this.credentials.username) {
        axios({
          method: 'POST',
            url: SERVER_URL + '/accounts/id-check/',
            data: this.credentials,
          })
          .then((res) => {
            this.credentials.idCheck = true
            alert(res.data.accept)
          })
          .catch((err) => {
            console.log(err.response.data.error)
            alert(err.response.data.error)
          })
        }
      // 아무 값도 입력되지 않았을 때
      else {
        alert('ID 값이 없습니다. ID를 입력해주세요.')
        this.credentials.idCheck = false
      }
    },
    // input이 바뀌면 idCheck를 새로 한다.
    changedid: function () {
      this.credentials.idCheck = false
    }
    
  },
}
</script>

<style>

</style>