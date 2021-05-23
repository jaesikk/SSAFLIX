<template>
  <div>
  <h1> Create </h1>
    <input type="text" v-model.trim="review.title"> | 
    <button @click="createReview">생성</button>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateReview',
  data: function () {
    return {
      review: {
        title: 'zz',    
        movie_title: 'dd',
        content: 'aa',
        // created_at: '',
        // updated_at: '',
        rank: '4',
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
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          }        
        }).then((res) => {
          console.log(res)
          this.$router.push({ name: 'Community' })

        }).catch((err) => {
          console.log(err.response)
        })
      }
    }
  }
}
</script>

<style>

</style>