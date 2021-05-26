import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import movieStore from './modules/movieStore'
import userStore from './modules/userStore'

Vue.use(Vuex)
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

const store = new Vuex.Store({
  // state: {
  //   accounts: {
  //     userId: '',
  //     username: '',
  //   },
  //   token: '',
  //   isLogin: false,
  // },
  // mutations: {

  //   ADD_USER: function (state, data) {
  //     state.accounts.userId = data.user.id
  //     state.accounts.username = data.user.username
  //     state.isLogin = true
  //     state.token = data.token
  //   },
  //   DELETE_USER: function (state) {
  //     state.accounts.userId = ''
  //     state.accounts.username = ''
  //     state.isLogin = false
  //     state.token= ''
  //   }
  // },
  // actions: {

  //   // credetials에 담아서 ADD_USER를 동작시킨다.
  //   loginUser: function (context, credentials) {
  //     axios({
  //       method: 'POST',
  //       url: SERVER_URL + '/accounts/api-token-auth/',
  //       data: credentials,
  //     }).then((res) => {
  //       context.commit('ADD_USER', res.data)
  //       // axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
  //       console.log(res.data)
  //       axios.defaults.headers.common['Authorization'] = `JWT ${context.state.token}`
  //       localStorage.setItem('jwt', res.data.token)
  //     })
  //   },
  //   logoutUser: function (context) {
  //     context.commit('DELETE_USER')
  //     localStorage.removeItem('jwt')
  //     // console.log(this.state.accounts)
  //   }
  // },
  modules: {
    movieStore: movieStore,
    userStore: userStore,
  },
  plugins: [  
    createPersistedState()
  ],
})
export default store