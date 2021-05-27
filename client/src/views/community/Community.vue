<template>
  <div id="commu-list" class="container fs-3">
    <img id="board" src="https://svg-clipart.com/svg/white/DabY6u8-chalk-board-vector.svg" alt="">
    <!-- {{ reviews }} -->
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateReview' }" class="navbar-brand d-flex justify-content-end p-5">게시글 생성</router-link>
      <div class="container">
        <div class="row fs-5">
          <div class="col">
            <p>| 영화</p>
          </div>
          <div class="col">
            <p>| 제목</p>
          </div>
          <div class="col">
            <p>| 작성자</p>
          </div>
        </div>
      </div>
    <br>
      <ol>
        <li v-for="review in reviews" :key="review.id" :review="review">
          <!-- {{ review }} -->
          <div id="review-list" class="container">
            <div class="row">
              <div class="col">
                {{ review.movie_title}}
              </div>
              <div class="col">
                <router-link
                  :to="{ name: 'ReviewDetail',
                      params: {reviewId: review.id, review: review}
                    }"
                  class="navbar-brand fs-2">
                  {{ review.title }}
                </router-link>
              </div>
              <div class="col">
                <p class="text-muted fs-4">{{ review.username }}</p>
              </div>
            </div>
          </div>
          <hr> 
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
#commu-list {
  display: inline-block;
  margin-top: 30px;
  width: 50%;
  text-align: center;
}

#board {
  opacity: 0.5;
  position: fixed;
  width: 60%;
  top: 5%;
  bottom: 0px;
  left: 20%;
  right: 0px;
  z-index: -1;
}
</style>