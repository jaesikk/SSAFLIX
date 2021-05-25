<template>
  <div>
    <h1>UPDATE</h1>
      <router-link :to="{ name: 'ReviewDetail', params: {reviewId: review.id, review: review} }" class="navbar-brand d-flex justify-content-end ml-3">back</router-link>
      {{ review.title }}
        <div class="text-muted">

          <div>
            <input type="text" v-model.trim="review.title"> | 
          </div>
          <div>
            <input type="text" v-model.trim="review.movie_title"> | 
          </div>
          <div>
            <input type="text" v-model.trim="review.content"> | 
          </div>
          <div>
            <input type="number" v-model.trim="review.rank"> | 
          </div> 
          <button @click="updateReview">생성</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'UpdateReview',
  props: {
    review: Object,
  },
  data: function () {
    return {
      nowReview: this.review,
    }
  },
  methods: {
    updateReview: function() {
      axios ({
        method: 'PUT',
        url: SERVER_URL + `/community/${this.review.id}/`,
        data: {
          title: this.nowReview.title,
          movie_title: this.nowReview.movie_title,
          content: this.nowReview.content,
          rank: this.nowReview.rank,
        },    
      }).then((res) => {
        console.log(res.data)
        this.nowReview = res.data
        this.$router.push({ name: 'ReviewDetail' })
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
  }
}
</script>

<style>

</style>