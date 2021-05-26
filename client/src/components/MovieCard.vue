<template>
  <div class="gui-card">
    <div class="gui-card__media">
      <img @click="selectMovie" class="gui-card__img" :src="poster" alt=""/>
      <!-- <router-link :to="{ name: 'MovieDetail' }" , params: {movieId: movie.id, movie: movie}, tag="img"
        @click="selectMovie" class="gui-card__img" :src="poster" alt=""
      >
      </router-link> -->
    </div>
    <div class="gui-card__details">
      <div class="gui-card__title">
        {{ movie.title }}
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },  
  data: function () {
    return {
      poster: "https://image.tmdb.org/t/p/w500/" + String(this.movie.poster_path)
    }
  },
  methods: {
    selectMovie: function () {
      // this.$emit('selectmovie', this.movie)
      this.$router.push({ name: 'MovieDetail', params: {movieId: this.movie.id, movie: this.movie}})
      console.log('select!!@!!')
    }
  }
}

</script>

<style>

</style>