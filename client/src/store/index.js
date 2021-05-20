import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    movies: [],
  },
  mutations: {
    ADD_MOVIE: function (state, movieList) {
      state.movies = movieList
    }
  },
  actions: {
    getMovies: function (context) {
      for (let i=1; i<5; i++) {
        axios({
          method: 'get',
          url: SERVER_URL + '/movies/',
        }).then((res) => {
          context.commit('ADD_MOVIE', res.data)
        })
      }
    },
    
  },
  modules: {
  }
})
