import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    accounts: {
      userId: '',
      username: '',
    },
    token: '',
    isLogin: false,
    movies: [],
  },
  mutations: {
    ADD_MOVIE: function (state, movieList) {
      state.movies = movieList
    },
    ADD_USER: function (state, data) {
      state.accounts.userId = data.user.id
      state.accounts.username = data.user.username
      state.isLogin = true
      state.token = data.token
    },
    DELETE_USER: function (state) {
      state.accounts.userId = ''
      state.accounts.username = ''
      state.isLogin = false
    }
  },
  actions: {
    getMovies: function (context) {
      axios({
        method: 'GET',
        url: SERVER_URL + '/movies/',
      }).then((res) => {
        context.commit('ADD_MOVIE', res.data)
      })
    },
    // credetials에 담아서 ADD_USER를 동작시킨다.
    loginUser: function (context, credentials) {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: credentials,
      }).then((res) => {
        context.commit('ADD_USER', res.data)
        // axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        axios.defaults.headers.common['Authorization'] = `JWT ${this.state.token}`
        localStorage.setItem('jwt', res.data.token)
        // console.log(this.state.accounts)
        // console.log('vuex')
        // console.log(res)
      })
    },
    logoutUser: function (context) {
      context.commit('DELETE_USER')
      localStorage.removeItem('jwt')
      // console.log(this.state.accounts)
    }
  },
  modules: {
  },
  plugins: [  
    createPersistedState()
  ],
})
