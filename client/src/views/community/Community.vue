<template>
  <div id="reviewlist" class="container fs-3">
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateReview' }" class="navbar-brand d-flex justify-content-end ml-3">게시글 생성</router-link>
    <ol>
      <li v-for="review in reviews" :key="review.id" :review="review">
        <router-link
        :to="{ name: 'ReviewDetail', params: {reviewId: review.id, review: review} }"
          class="navbar-brand">{{ review.title }}</router-link> <hr> 
      </li>
    </ol>
    <!-- <CommunityDetail v-for="review in reviews" :key="review.id" :review="review" /> -->
    <!-- <button @click="getReviews" > 정보 가져오기</button> -->
  </div>
</template>

<script>
import axios from 'axios'
// import CommunityDetail from '@/components/CommunityDetail.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Community',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  components: {
    // CommunityDetail,
  },
  data: function () {
    return {
      reviews: [],
    }
  },
  methods: {
    getReviews: async function (){
      try{
        const res = await axios({
          method: 'GET',
          url: SERVER_URL + '/community/create/',     
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          }
        })
        // console.log(res)
        // console.log(res.data)
        console.log('getReviews')
        this.reviews = res.data
      } catch (err) {
        console.log(err.response)
      }
    },
  },
  mounted: function () {
    if (this.isLogin) {
      this.getReviews()
    } else {
      this.$router.push({ name: 'Login' })
      alert('로그인이 필요합니다.')
    }
    // this.getReviews()
  }
}
</script>

<style>
#reviewlist {
  display: inline-block;
  width: 50%;
  text-align: center;
}
</style>