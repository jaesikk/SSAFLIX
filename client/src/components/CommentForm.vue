<template>
  <div>
    <input type="text" v-model="comment" placeholder="댓글을 입력하세요." @keyup.enter="createComment">
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {


  name: 'CommentForm',
  props: {
    review: Object,
  },
  data: function () {
    return {
      comment: '',
    }
  },
  methods: {
    // data를 {}로 감싸주어 형태에 맞게 접근
    createComment: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + `/community/${this.review.id}/comments/`,
        data: {content: this.comment},
      }).then((res) => {
        this.$emit('getComments')
        console.log(res)
      }).catch((err) => {
        console.log(err.response)
      })
    },
  }
}
</script>

<style>

</style>