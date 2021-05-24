<template>
<div class="container">
  <div class="home slider">
    <div class="container">

    <span onmouseover="scrollEsquerda()" onmouseout="clearScroll()" class="handle handlePrev active">
      <i class="fa fa-caret-left" aria-hidden="true"></i>
    </span>
      <div id="scroller" class="row">
        <div class="row__inner">
         <MovieCard v-for="movie in movies" :key="movie.pk" :movie='movie'/>
       </div>
      </div>
    <span onmouseover="scrollDireita()" onmouseout="clearScroll()"  class="handle handleNext active">
      <i class="fa fa-caret-right" aria-hidden="true"></i>
    </span>
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
  mounted: function () {
    this.$nextTick(function () {
      this.$store.dispatch('getMovies')
      console.log('getMovies_Home.vue')
    })
  },
  computed: {
    ...mapState(['movies'])
  }
}
</script>
