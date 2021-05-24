import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    accounts: '',
    movies: [],
  },
  mutations: {
    ADD_MOVIE: function (state, movieList) {
      state.movies = movieList
    },
    ADD_USER: function (state, userId) {
      state.accounts = userId
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
    getUser: function (context, credentials) {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: credentials,
      }).then((res) => {
        context.commit('ADD_USER', res.data.userId)
        localStorage.setItem('jwt', res.data.token)
        console.log(this.state.accounts)
        console.log('vuex')
        console.log(res)
      })
    }
  },
  modules: {
  }
})
