<template>
  <div>
    <p>{{ review.title }}</p>
    <p>{{ review.content }}</p>
    <button @click="liked"> 좋아요 </button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'CommunityDetail',
  data: function() {
    return {
      // isLike = 
    }
  },
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  method: {
    liked: function() {
      axios ({
        method: 'POST',
        url: SERVER_URL + `/community/${this.review.pk}/like/`,
        data: this.review,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }     
      }).then((res) => {
        console.log(res.data)
      }).catch((err) => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style>

</style>