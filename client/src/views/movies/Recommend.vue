<template>
  <div>
    <h1>추천 영화 페이지</h1>
    <button @click="randomRecommend">오늘의 랜덤 영화 추천</button>
    <p>오늘의 추천 영화는 ??</p>
    <div v-show="isRandomClick">
      <img :src="poster" alt="movie_poster">
      <p>{{ movie.title }} !</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Recommend',
  data: function () {
    return {
      movie: [],
      poster: '',
      isRandomClick: false,
    }
  },
  methods: {
    randomRecommend: function () {
      const rndIdx = _.random(1, this.popularMovies.length)
      axios({
        method: 'GET',
        url: SERVER_URL + `/movies/${rndIdx}/`
      }).then((res) => {
        console.log(res)
        this.movie = res.data
        this.poster = "https://image.tmdb.org/t/p/w400/" + String(this.movie.poster_path)
        this.isRandomClick = true
      }).catch((err) =>{
        console.log(err.response)
      })
    },
  },
  computed: {
    ...mapState('movieStore', ['popularMovies'])
  }
}
</script>

<style>

</style>