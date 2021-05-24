<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateReview' }" class="navbar-brand d-flex justify-content-end ml-3">게시글 생성</router-link>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        <router-link
        :to="{ name: 'ReviewDetail',
        params: {
          reviewTitle: review.title,
          reviewContent: review.content,
          } }"
          class="navbar-brand">{{ review.title }}</router-link> |
        <button @click="delReview(review)">X</button>
  
      </li>
    </ul>
    <CommunityDetail v-for="review in reviews" :key="review.id" :review="review" />
    <button @click="getReviews" > 정보 가져오기</button>
  </div>
</template>

<script>
import axios from 'axios'
import CommunityDetail from '@/components/CommunityDetail.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Community',
  components: {
    CommunityDetail,
  },
  data: function () {
    return {
      reviews: [],
    }
  },
  methods: {
    getReviews: async function (){
      const res = await axios({
        method: 'GET',
        url: SERVER_URL + '/community/create/'
      })
      console.log(res)
      console.log('getReviews')
      this.reviews = res.data
    },
    delReview: function (review) {
      axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${review.id}/`,
      })
      .then((res) => {
        this.getReviews()
        console.log(res)
      })
      .catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    // updateReviews: function (review) {
    //   axios({
    //     method: 'PUT',
    //     url: SERVER_URL + `community/${review.id}/`
    //   }).then((res) => {
    //     console.log(res)
    //     console.log('updated')
    //     this.getReviews()
    //   })
    // }
  },
  created: function () {
    // if (this.isLogin) {
    //   console.log('isLogin')
    //   this.getReviews()
    // } else {
    //   this.$router.push({ name: 'Login' })
    //   alert('로그인이 필요합니다.')
    // }
    this.getReviews()
  }
}
</script>

<style>

</style>