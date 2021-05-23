import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    accounts: [],
    movies: [],
  },
  mutations: {
    ADD_MOVIE: function (state, movieList) {
      state.movies = movieList
    },
    
  },
  actions: {
    getMovies: function (context) {
      axios({
        method: 'get',
        url: SERVER_URL + '/movies/',
      }).then((res) => {
        context.commit('ADD_MOVIE', res.data)
      })
    },
    
  },
  modules: {
  }
})
