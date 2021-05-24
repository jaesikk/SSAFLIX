<template>
  <div>
  <h1> Create </h1>
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
      <button @click="createReview">생성</button>
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
        title: '글 제목',    
        movie_title: '영화 제목',
        content: '글 내용',
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

</style>