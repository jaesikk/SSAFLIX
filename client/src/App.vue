<template>
  <div id="app">
    <div id="nav">
       <!-- nav bar -->
      <nav class="navbar fixed-top navbar-expand-lg navbar-dark p-2">
        <div class="container">
          <router-link to="/" class="navbar-brand">Home</router-link> |
          <router-link :to="{ name: 'Recommend' }" class="navbar-brand">Recommend</router-link> |
          <router-link :to="{ name: 'Community' }" class="navbar-brand">Community</router-link> |
          
          <span v-if="isLogin">
           <router-link to="#" @click.native="onLogout" class="navbar-brand">Logout</router-link>
          </span>
          <span v-else>
            <router-link :to="{ name: 'Login' }" class="navbar-brand">Login</router-link> |
            <router-link :to="{ name: 'Signup' }" class="navbar-brand">Signup</router-link>
          </span>
        </div>
      </nav>
    </div>
    <router-view @login="onLogin" :isLogin="isLogin"/>
    <!-- 로그인  -->
  </div>
</template>


<script>
import axios from 'axios'
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    onLogin: function () {
      this.isLogin = true
      axios.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('jwt')}`
    },
    onLogout: function () {
      localStorage.removeItem('jwt')
      this.isLogin = false
      this.$router.push({ name: 'Login' })
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  // 토큰을 가져오고, 있다면 onLogin 실행한다
  created: function () {
    const jwt = localStorage.getItem('jwt')
    if (jwt) {
      this.onLogin()
    }
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
  color: #ced1d4a9;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #f1f2f3d2;
}

#nav a.router-link-exact-active {
  color: #bd2626;
}
</style>
