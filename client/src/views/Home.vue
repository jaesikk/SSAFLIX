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
          <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            <MovieCard 
              v-for="movie in movies"
              :key="movie.pk"
              :movie='movie'
              @selectmovie="onSelect"
            />
          </button>

        </div>
      </div>
    <span onmouseover="scrollDireita()" onmouseout="clearScroll()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>

    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">영화제목</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>%%%%OVERVIEW%%%</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    </div>

  </div>
</div>
</template>

<script>
// @ is an alias to /src
// import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'


export default {
  name: 'Home',
  components: {
    MovieCard
  },
  data: function () {
    return {
      selectMovie: '',
    }
  },
  methods: {
    onSelect: function (movie) {
      this.selectMovie = movie
      console.log(this.selectMovie)
      console.log('onSelect@@!@@')
    },
  },
  mounted: function () {
    this.$nextTick(function () {
      this.$store.dispatch('getMovies')
    })
  },
  computed: {
    ...mapState(['movies'])
  },
}
</script>
