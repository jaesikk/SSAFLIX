<template>
  <div class="container">
    <h1>UPDATE</h1>
    <hr>
      <router-link :to="{ name: 'ReviewDetail', params: {reviewId: review.id, review: review} }" class="navbar-brand d-flex justify-content-end ml-3">back</router-link>
        <div id="input">
          <div class="input-group input-group-sm mb-3">
            <span class="input-group-text" id="inputGroup-sizing-sm">글 제목</span>
            <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model.trim="review.title">
          </div>
          <div class="input-group input-group-sm mb-3">
            <span class="input-group-text" id="inputGroup-sizing-sm">영화 제목</span>
            <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model.trim="review.movie_title">
          </div>
          <div class="input-group input-group-sm mb-3">
            <span class="input-group-text" id="inputGroup-sizing-sm">글 내용</span>
            <textarea class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" style="height: 360px" v-model.trim="review.content"></textarea>
          </div>
          <div class="input-group input-group-sm mb-3">
            <span class="input-group-text" id="inputGroup-sizing-sm">평점</span>
            <input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model.trim="review.rank">
          </div>
          <button class="btn btn-outline-primary" @click="updateReview">생성</button>
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
        this.$router.push({ name: 'Community' })
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
  },
}
</script>

<style>
/*  */
</style>