<template>
  <div>
    <h1>{{ review.title }}</h1>
    <div class="d-flex justify-content-end ml-3">
      <button @click="updateReviews">upd</button> |
      <button @click="delReview(review)">del</button> |
      <router-link :to="{ name: 'Community' }">back</router-link>
    </div>
    <hr>
    <p>{{ review.id }}</p>
    <h2>{{ review.movie_title }} 후기</h2>
      <p>평점: {{ review.rank }}</p>
      <p>글 내용: {{ review.content }}</p>
    <!-- <button @click="checkId">버튼</button> -->
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
    updateReviews: function (review) {
      axios({
        method: 'PUT',
        url: SERVER_URL + `community/${review.id}/`
      }).then((res) => {
        console.log(res)
        console.log('updated')
        this.getReviews()
      })
    },
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
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkId: function () {
      console.log((this.$store.state.accounts))
    },
  }
}
</script>

<style>

</style>