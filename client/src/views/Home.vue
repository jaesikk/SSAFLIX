<template>
<div>
  <h1>상영</h1>
  <!-- <button @click="onDark">다크모드</button> -->
  <div class="home slider">
    <div class="container">
    <!-- popularMovies -->
    <span id="popluar" onmouseover="scrollEsquerda1()" onmouseout="clearScroll1()" class="handle handlePrev active">
      <i class="fa fa-caret-left" aria-hidden="true"></i>
    </span>
      <div id="scroller1" class="row">
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
    <span id="popluar" onmouseover="scrollDireita1()" onmouseout="clearScroll1()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>
    </div>

    <h2>명작</h2>
    <!-- topRatedMovies -->
    <span id="sample" onmouseover="scrollEsquerda2()" onmouseout="clearScroll2()" class="handle handlePrev active">
      <i class="fa fa-caret-left" aria-hidden="true"></i>
    </span>
      <div id="scroller2" class="row">
        <div class="row__inner">
          
          <!-- Button trigger modal -->
          <button type="button" class="btn btn-dark">
            <MovieCard 
              v-for="movie in topRatedMovies"
              :key="movie.pk"
              :movie='movie'
              @selectmovie="onSelect"
            />
          <!-- </router-link> -->
          </button>

        </div>
      </div>
    <span id="sample" onmouseover="scrollDireita2()" onmouseout="clearScroll2()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>

    <h2>다가오는 영화</h2>
    <span id="upcoming" onmouseover="scrollEsquerda3()" onmouseout="clearScroll3()" class="handle handlePrev active">
      <i class="fa fa-caret-left" aria-hidden="true"></i>
    </span>
      <div id="scroller3" class="row">
        <div class="row__inner">
          
          <!-- Button trigger modal -->
          <button type="button" class="btn btn-dark">
            <MovieCard 
              v-for="movie in upcomingMovies"
              :key="movie.pk"
              :movie='movie'
              @selectmovie="onSelect"
            />
          <!-- </router-link> -->
          </button>
        </div>
      </div>
    <span id="upcoming" onmouseover="scrollDireita3()" onmouseout="clearScroll3()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>
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
      checkDark: true,
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
    // onDark: function () {
    //   if (checkDark){
    //     // body on 
    //   }
    //   else {
    //     // body off or body2
    //   }
    // },
  },
  mounted: function () {
    this.$store.dispatch('movieStore/getMovies', 'popular')
    this.$store.dispatch('movieStore/getMovies', 'topRated')
    this.$store.dispatch('movieStore/getMovies', 'upcoming')
    // this.$nextTick(function () upcoming{
    // })
  },
  computed: {
    ...mapState('movieStore', ['popularMovies']),
    ...mapState('movieStore', ['topRatedMovies']),
    ...mapState('movieStore', ['upcomingMovies']),
  },
}
</script>

<style>
#sample {
  position: absolute;
  top: 350%;
}
#upcoming {
  position: absolute;
  top: 700%;
}
</style>