<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateReview' }" class="navbar-brand">게시글 생성</router-link>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        {{ review.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Community',
  data: function () {
    return {
      reviews: [],
    }
  },
  methods: {
    getReviews: async function (){
      const res = await axios({
        method: 'GET',
        url: SERVER_URL + '/coummunity/create/'
      })
      this.reviews = res.data
    },

  }
}
</script>

<style>

</style>