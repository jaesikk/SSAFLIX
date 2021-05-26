<template>
<div class="container">
  <h1>상영</h1>
  <div class="home slider">
    <div class="container">
      
    <span onmouseover="scrollEsquerda()" onmouseout="clearScroll()" class="handle handlePrev active">
      <i class="fa fa-caret-left" aria-hidden="true"></i>
    </span>
      <div id="scroller" class="row">
        <div class="row__inner">
          
          <!-- Button trigger modal -->
          <!-- <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#staticBackdrop"> -->
          <button type="button" class="btn btn-dark">
          <!-- <router-link :to="{ name: 'MovieDetail' }" , params: {selectMovieId: selectMovie.id, selectMovie: selectMovie}, tag="a"> -->
            <MovieCard 
              v-for="movie in popularMovies"
              :key="movie.pk"
              :movie='movie'
              @selectmovie="onSelect"
            />
          <!-- </router-link> -->
          </button>

        </div>
      </div>
    <span onmouseover="scrollDireita()" onmouseout="clearScroll()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>
    </div>

    <!-- Modal -->
    <!-- <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">{{ selectMovie.title}}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
            <div class="modal-body">
              <p>{{ selectMovie.release_date }}</p>
              <p>{{ selectMovie.popularity }}</p>
              <p>{{ selectMovie.vote_count }}</p>
              <p>{{ selectMovie.vote_average }}</p>
              <p>{{ selectMovie.poster_path }}</p>
              <p>{{ selectMovie.tmdb_id }}</p>
              <div class="video-container">
                <iframe 
                  id="ytplayer" 
                  type="text/html"
                  :src="videoURI"
                  frameborder="0">
                </iframe>
              </div>
            </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>

        </div>
      </div>
    </div> -->


  </div>
</div>
</template>

<script>
// @ is an alias to /src
// import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const movieStore = 'movieStore'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  data: function () {
    return {
      selectMovie: '',
      // videoList: [],
      // videoURI: '',
    }
  },
  methods: {
    onSelect: function (movie) {
      this.selectMovie = movie
      // console.log(this.selectMovie)
      console.log('onSelect@@!@@')
      // axios({
      //   methods: 'GET',
      //   url: SERVER_URL + `/movies/${this.selectMovie.id}/videos/`
      // }).then((res) => {
      //   this.videoList = res.data
      //   console.log(this.videoList)
      //   this.videoURI = `https://www.youtube.com/embed/${this.videoList[0].key}}`
      // }).catch((err) => {
      //   console.log(err.response)
      // })
    },
  },
  mounted: function () {
    this.$store.dispatch('movieStore/getMovies', 'popular')
    console.log('getMovies_Home.vue')
    // this.$nextTick(function () {
    // })
  },
  computed: {
    ...mapState('movieStore', ['popularMovies'])
  },
}
</script>
