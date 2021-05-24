<template>
  <div>
    <p>{{ review.title }}</p>
    <p>{{ review.content }}</p>
    <button @click="onLiked" >{{ isLike ? '좋아요 취소' : '좋아요'}} </button>
    <!-- <p>{{ isLike }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'CommunityDetail',
  data: function() {
    return {
      isLike: '',
    }
  },
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  methods: {
    onLiked: function() {
      axios ({
        method: 'POST',
        url: SERVER_URL + `/community/${this.review.id}/like/`,
        data: this.review,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }     
      }).then((res) => {
        console.log(res.data)
        this.isLike = res.data.isLike
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
  },
  mounted:  function() {
    axios ({
      method: 'GET',
      url: SERVER_URL + `/community/${this.review.id}/like/`,
      data: this.review,
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      }     
    }).then((res) => {
      // console.log(res.data)
      this.isLike = res.data.isLike
    }).catch((err) => {
      console.log(err.response)
      // alert(err.response.data.error)
    })
  }   
}
</script>

<style>

</style>