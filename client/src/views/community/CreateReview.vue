<template>
  <div>
  <h1> Create </h1>
    <input type="text" v-model.trim="posts.title"> | 
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
      posts: {
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
      const review = {
        posts: this.posts,
      }
      if (review.posts) {
        axios({
          method: 'POST',
          url: SERVER_URL + '/community/create/',
          data: review,
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          }        
        }).then((res) => {
          console.log(res)
          this.$router.push({ name: 'Community' })

        }).catch((err) => {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style>

</style>