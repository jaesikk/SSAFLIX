<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar fixed-top navbar-expand-lg navbar-dark p-2">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand"><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="NETFLIX" style= "width:120px"></router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link to="/" class="nav-link">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Recommend' }" class="nav-link">Recommend</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Community' }" class="nav-link">Community</router-link>
              </li>
            </ul>

            <div class="d-flex">
              <span v-if="isLogin">
                <router-link to="#" @click.native="onLogout" class="nav-link">Logout</router-link>
              </span>
              <span v-else>
                <router-link :to="{ name: 'Login' }" class="nav-link">Login</router-link> 
                <!-- <router-link :to="{ name: 'Signup' }" class="nav-link">Signup</router-link> -->
              </span>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <router-view @login="onLogin" :isLogin="isLogin"/>
    <!-- 로그인  -->
    
  </div>
</template>


<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'App',

  data: function () {
    return {
      // isLogin: false,
    }
  },
  methods: {
    onLogin: function () {
      // this.isLogin = true
      // console.log(this.$store.state.isLogin)
      // console.log(this.$store.state.accounts)
      axios.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('jwt')}`
    },
    onLogout: function () {
      localStorage.removeItem('jwt')
      // this.isLogin = false
      this.$store.dispatch('userStore/logoutUser')
      axios.defaults.headers.common['Authorization'] = ''
      console.log(axios.defaults.headers.common['Authorization'])
      this.$router.push({ name: 'Login' })
    },
  },
  // 토큰을 가져오고, 있다면 onLogin 실행한다
  created: function () {
    const jwt = localStorage.getItem('jwt')
    if (jwt) {
      this.onLogin()
    }
  },
  computed: {
    ...mapState('userStore', ['isLogin'])
  }
}
</script>

<style>


#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  padding: 0px 50px;
  margin-bottom: 70px;
}

#nav a {
  font-weight: bold;
  color: #f1f2f3d2;
}

#nav a.router-link-exact-active {
  color: #bd2626;
}
</style>
