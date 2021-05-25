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
            <MovieCard v-for="movie in movies" :key="movie.pk" :movie='movie'/>
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
            <h5 class="modal-title" id="staticBackdropLabel"><li v-for="movie in movies" :key="movie.pk">{{movie.title}}</li></h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>안녕하세요%%%%%%%</p>
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
      movie: '',
    }
  },
  method: {
    // onClick: function (movie) {
    //   this.movie = movie
    //   console.log('here')
    // }
  },
  mounted: function () {
    this.$store.dispatch('getMovies')
    console.log('getMovies_Home.vue')
    // this.$nextTick(function () {
    // })
  },
  computed: {
    ...mapState(['movies'])
  },
}
</script>
