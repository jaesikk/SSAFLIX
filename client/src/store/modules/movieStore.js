import axios from "axios"

const SERVER_URL = process.env.VUE_APP_SERVER_URL
// async function return promise
const movieStore = {
  namespaced: true,
  state: {
    popularMovies: [],
    topRatedMovies: [],
    upcomingMovies: [],
  },
  mutations: {
    ADD_MOVIE: function (state, payload) {
      // console.log(payload.query)
      if (payload.query === 'popular')
        state.popularMovies = payload.movieList
      else if (payload.query === 'topRated')
        state.topRatedMovies = payload.movieList
      else if (payload.query === 'upcoming')
        state.upcomingMovies = payload.movieList
      // console.log(state.popularMovies)
      // console.log(payload.movieList)
    },
  },
  actions: {
    getMovies(context, queryString) {
      const str = queryString
      return axios({
        method: 'POST',
        url: SERVER_URL + '/movies/',
        data: {
          query: queryString
        }
  
      }).then((res) => {
        // console.log(res.data)
        context.commit('ADD_MOVIE', { movieList: res.data, query: str })
      }).catch((err) => {
        console.log(err.response)
      })
    },
  },
}

export default movieStore