<template>
  <div class="container">
    <h1>{{ review.title }}</h1>
    <router-link :to="{ name: 'Profile', params: {reviewUser: review.user, review: review}}" class="btn btn-link d-flex justify-content-end ml-3">go profile</router-link>

    <div class="d-flex justify-content-between">
        <button class="btn btn-primary" @click="onLiked" ><i class="fa-thumbs-up" :class="[ isLike ? 'fas' : 'far']"></i> </button>
        <div>
        <router-link :to="{ name: 'Community' }" class="btn btn-link">back</router-link>
          <div v-if="checkReviewId">
            <router-link :to="{ name: 'UpdateReview', params: {reviewId: review.id, review: review} }"><button class="btn btn-sm btn-outline-info">수정</button></router-link> |
            <button class="btn btn-sm btn-outline-info" @click="delReview(review)">삭제</button>
          </div>
        </div>
    </div>
    <hr>
    <!-- <p>{{ review.id }}</p> -->
      <div id="date">
        <p>작성일: {{ review.created_at }}</p>
        <p>수정일: {{ review.updated_at }}</p>
      </div>
      <h2>영화: {{ review.movie_title }}</h2>
      <div id="content">
        <ul id="review">
          <p>평점: {{ review.rank }}</p>
          <p>글 내용: {{ review.content }}</p>
        </ul>
      </div>
    <!-- <button @click="checkId">CHECKID버튼</button> -->
    <hr>
    <div>
      <CommentForm @getComments="getComments" :review="review"/>
      <!-- commetn.id를 키값으로 v-for문 comment 접근 -->
      <br>
      <ul>
        <li v-for="(comment) in comments" :key="comment.id" class="row">
          <span class="col text-muted" >익명{{ comment.user }} |</span>
          <span class="col">{{ comment.content }}</span>
          <span class="col text-muted ">
            | {{ comment.created_at }} 
            <!-- comment.user와 accounts.userId를 통해 체크하는데 이슈가 있음 -->
            <!-- <button @click="checkComment(comment, idx)">check</button> -->
            <button class="btn btn-sm btn-outline-light" @click="delComment(comment)">X</button>
          </span>
          <hr>
        </li>
      </ul>
    </div>
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
      checkReviewId: false,
      // checkCommentUser: false,
    }
  },
  computed: {
    ...mapState('userStore', ['accounts'])
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
    // accounts.userId와 review.user 같을때만 수정, 삭제기능을 활성화
    checkId: function () {
      if (this.accounts.userId === this.review.user) {
        this.checkReviewId = true
        console.log('checkId')
      }
      else {
        this.checkReviewId = false
        console.log('checkIdfail')
      }
    },
    // checkComment: function (comment, idx) {
    //   console.log(this.comments[idx].user)
    //   console.log(comment.user)
    //   if (this.accounts.userId === comment.user) {
    //     this.checkCommentUser = true
    //     console.log('true')
    //   }
    //   else {
    //     this.checkCommentUser = false
    //     console.log('fail')
    //   }
    // },
  },
  // 댓글과 ID체크 바로 호출
  mounted: function () {
    this.getComments()
    this.checkId()
    axios ({
        method: 'GET',
        url: SERVER_URL + `/community/${this.review.id}/like/`,
      }).then((res) => {
        console.log(res.data)
        this.isLike = res.data.isLike
        // this.getReviews()
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
  }
}
</script>

<style>
#content {
  height: 300px;
  left: 10%;
}

#review {
  left: 100px;
}

#date {
  display: inline-block;
  width: 30%;
  text-align: end;

}
</style>