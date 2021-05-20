<template>
  <div class="gui-card">
    <div class="gui-card__media">
      <img class="gui-card__img" :src="poster" alt=""  />
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
  }
}

</script>

<style>

</style>