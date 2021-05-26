<template>
  <div>
    <h1>{{ review.title }}</h1>
    <router-link :to="{ name: 'Profile', params: {reviewUser: review.user, review: review}}">작성자 프로필로 이동</router-link>
    <!-- {{ review }} -->
    
    <div class="d-flex justify-content-between">
        <button @click="onLiked" >{{ isLike ? '좋아요 취소' : '좋아요'}} </button>
        <div>
        <router-link :to="{ name: 'Community' }">back</router-link>
          <div v-if="check">
            <router-link :to="{ name: 'UpdateReview', params: {reviewId: review.id, review: review} }">수정</router-link> |
            <button @click="delReview(review)">삭제</button>
          </div>
        </div>
    </div>
    <hr>
    <p>{{ review.id }}</p>
    <h2>{{ review.movie_title }} 후기</h2>
      <p>평점: {{ review.rank }}</p>
      <p>글 내용: {{ review.content }}</p>
    <!-- <button @click="checkId">CHECKID버튼</button> -->
    <hr>
    <div>
      <CommentForm @getComments="getComments" :review="review"/>
      <!-- commetn.id를 키값으로 v-for문 comment 접근 -->
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.content }}
          <button @click="delComment(comment)">X</button>
        </li>
      </ul>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import CommentForm from '@/components/CommentForm.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  components: {
    CommentForm,
  },
  props: {
    review: Object,
  },
  data: function () {
    return {
      comments: [],
      isLike: '',
      nowReview: this.review,
      isFollow: '',
      check: false,
    }
  },
  computed: {
    ...mapState(['accounts'])
  },
  methods: {
    delReview: function (review) {
      axios({
        method: 'delete',
        url: SERVER_URL + `/community/${review.id}/`,
      })
      .then(() => {
        this.$router.push({ name: 'Community' })
        this.getReviews()
      })
      .catch((err) => {
        alert(err.response.data.error)
      })
    },
    //
    // review.id가 router에서 props Object()로 감싸주어 review에 접근하지 못했었음
    // CommentForm에서 emit을 받아와 getComments
    getComments: function () {
      axios({
        method: 'GET',
        url: SERVER_URL + `/community/${this.review.id}/comments/`,
      })
      . then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    delComment: function (comment) {
      axios({
        method: 'DELETE',
        url: SERVER_URL + `/community/${this.review.id}/comments/${comment.id}/`,
      })
      .then((res) => {
        console.log('get')
        this.getComments()
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
        alert(err.response.data.error)
      })
    },
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
    checkId: function () {
      if (this.$store.state.accounts.userId === this.review.user) {
        this.check = true
      }
      else {
        this.check = false
      }
    },
  },
  // 댓글과 ID체크 바로 호출
  mounted: function () {
    this.getComments()
    this.checkId()
  }
}
</script>

<style>

</style>