<template>
  <div>
    <p>{{ nowReview.title }}</p>
    <p>{{ nowReview.content }}</p>
    <button @click="onLiked" >{{ isLike ? '좋아요 취소' : '좋아요'}} </button>
    <button @click="onFollow" >{{ isFollow ? '팔로우 취소' : '팔로우'}} </button>
    <button @click="onUpdate" > 수정 </button>
    <button @click="onDelete" > 삭제 </button>
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
      nowReview: this.review,
      isFollow: '',
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
      }).then((res) => {
        console.log(res.data)
        this.isLike = res.data.isLike
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    onFollow: function() {
      axios ({
        method: 'POST',
        url: SERVER_URL + `/accounts/${this.nowReview.user}/follow/`,
      }).then((res) => {
        console.log(res.data)
        this.isFollow = res.data.isFollow
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    onUpdate: function() {
      axios ({
        method: 'PUT',
        url: SERVER_URL + `/community/${this.review.id}/`,
        data: {
          title: this.nowReview.title,
          movie_title: this.nowReview.movie_title,
          content: this.nowReview.content + '_수정됨',
          rank: this.nowReview.rank,
        },    
      }).then((res) => {
        console.log(res.data)
        this.nowReview = res.data
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    onDelete: function() {
      axios ({
        method: 'DELETE',
        url: SERVER_URL + `/community/${this.review.id}/`,
        data: this.review,
      }).then((res) => {
        console.log(res.data)
        this.review = res.data
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    
  },
  mounted: function() {
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
    axios ({
      method: 'GET',
      url: SERVER_URL + `/accounts/${this.nowReview.user}/follow/`,
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      }     
    }).then((res) => {
      // console.log(res.data)
      this.isFollow = res.data.isFollow
    }).catch((err) => {
      console.log(err.response)
      // alert(err.response.data.error)
    })
  },
  // computed: {
  //   changeReview: function () {
  //     return this.review
  //   }
  // }   
}
</script>

<style>

</style>