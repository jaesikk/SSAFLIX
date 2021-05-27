<template>
  <div class="container">
  <h1> Create </h1>
  <hr>
    <router-link :to="{ name: 'Community' }" class="d-flex justify-content-end ml-3">back</router-link>

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
      <!-- <div class="input-group input-group-sm mb-3">
        <span class="input-group-text" id="inputGroup-sizing-sm">글 내용</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model.trim="review.content">
      </div> -->
      <div class="input-group input-group-sm mb-3">
        <span class="input-group-text" id="inputGroup-sizing-sm">평점</span>
        <input type="number" class="form-control" placeholderaria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model.trim="review.rank">
      </div>
      <button class="btn btn-outline-primary" @click="createReview">생성</button>
    </div>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateReview',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  data: function () {
    return {
      review: {
        title: '',    
        movie_title: '',
        content: '',
        created_at: '',
        updated_at: '',
        rank: '',
      }
    }
  },
  methods: {
    createReview: function () {
      // const reviewItem = {
      //   review: this.review,
      // }
      // console.log(reviewItem.review)
      if (this.review) {
        axios({
          method: 'POST',
          url: SERVER_URL + '/community/create/',
          data: this.review,
          // headers: {
          //   Authorization: `JWT ${localStorage.getItem('jwt')}`
          // }        
        }).then((res) => {
          console.log(res)
          this.$router.push({ name: 'Community' })
        }).catch((err) => {
          console.log(err.response)
        })
      }
    }
  },
  created: function () {
    if (!this.isLogin) {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
#input {
  position: absolute;
  width: 40%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>