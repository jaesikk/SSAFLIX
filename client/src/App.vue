<template>
  <div id="app" class="wrapper">
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
                <router-link to="/" class="nav-link text-decoration-none">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Recommend' }" class="nav-link text-decoration-none">Recommend</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Community' }" class="nav-link text-decoration-none">Community</router-link>
              </li>
            </ul>

            <div class="d-flex">
              <button @click="changeDarkMode" :style="{ color: isDark? '#f1f2f3d2' : '#16181a'}" class="btn btn-toggle" data-toggle="button" aria-pressed="false" autocomplete="off">
                {{isDark ? 'White Mode' : 'Dark Mode'}}  
              </button>
              <!-- <p>{{ Number(accounts.userId) }}</p> -->
              <span id="nav-login" v-if="isLogin">
                <router-link :to="{ name: 'Profile', params: {reviewUser: Number(accounts.userId), review: accounts}}" class="btn btn-link ml-3 text-decoration-none">{{ accounts.username }}</router-link>
                <router-link to="#" @click.native="onLogout" class="nav-link text-decoration-none">Logout</router-link>
              </span>
              <span v-else>
                <router-link :to="{ name: 'Login' }" class="nav-link text-decoration-none">Login</router-link> 
                <!-- <router-link :to="{ name: 'Signup' }" class="nav-link">Signup</router-link> -->
              </span>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <router-view @login="onLogin" :isLogin="isLogin"/>
    <!-- 로그인  -->
    <!-- <footer id="footer" class="footer mt-auto py-3 sticky-bottom m-3">
      <div class="container text-muted fs-6">
        <ul href="">투자 정보  |  회사 정보</ul>
        <ul href="">문의 하기   |  이용 약관</ul>
        <span> 고객센터 : 042-820-7399  |</span>
        <span> 주소 : 대한민국 대전광역시 삼성화재연수원 SSAFY 대전캠퍼스</span>
      </div>
    </footer> -->
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
      isDark: true,
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
    changeDarkMode: function () {
      if (this.isDark === true){
        document.body.style.background = 'whitesmoke'
        document.body.style.color = '#16181a'
        // document.querySelectorAll('#nav a').forEach(a => {
        //   // a.style.color = '#16181a'
        //   a.classList.add('fontDark')
        //   a.classList.remove('fontWhite')
        // })
        // document.querySelector('.router-link-exact-active').color = '#bd2626'
      } else {
        document.body.style.background = '#16181a'
        document.body.style.color = '#f1f2f3d2'
        // document.querySelectorAll('#nav a').forEach(a => {
        //   // a.style.color = '#f1f2f3d2'
        //   a.classList.remove('fontDark')
        //   a.classList.add('fontWhite')
        // })
        // document.querySelector('.router-link-exact-active').color = '#bd2626'
        // console.log(document.querySelectorAll('#nav a'))
      }
      this.isDark = !this.isDark
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
    ...mapState('userStore', ['isLogin', 'accounts'])
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
  margin: 0px 50px;
  margin-bottom: 70px;
}



#nav a {
  font-weight: bold;
  color: inherit;
  /* color: #f1f2f3d2; */
  /* color: beige; */
}

#nav-login {
  display: flex;
}
/* #nav a.fontDark {
  color: #16181a;
}

#nav a.fontWhite {
  color: #f1f2f3d2;
} */

/* #nav a.navbar-dark .navbar-nav .nav-link {
  color: #f1f2f3d2;
} */

/* #nav a.nav-link{
  color: #f1f2f3d2;
}
#nav a.btn-link{
  color: #f1f2f3d2;
} */

#nav a.router-link-exact-active {
  color: #bd2626;
}

#footer {
  position: absolute;
  left: 32%;
  bottom: 0;
}

.wrapper {
  height: 100%;
}

.container-fluid {
  margin: 0px 60px;
}
</style>

