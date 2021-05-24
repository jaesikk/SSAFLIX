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
      <CommentForm :review="review"/>
      <ul>
        <!-- <CreateComment v-for="comment in comments" :key="comment.id" :review="review" /> -->
      </ul>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import CommentForm from '@/components/CommentForm.vue'
// import CreateComment from '@/components/CreateComment.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  components: {
    CommentForm,
    // CreateComment,
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
    getComments: function () {
      axios({
        method: 'GET',
        url: SERVER_URL + `/community/${this.review.id}/comments/`,
      })
      . then((res) => {
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