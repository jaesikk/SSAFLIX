<template>
  <div id="comment-input">
    <input class="form-control" type="text" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model="comment" placeholder="댓글을 입력하세요." @keyup.enter="createComment">
    <button @click="createComment" class="btn btn-sm btn-outline-light" style="width:50px">댓글</button>
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
        this.comment= ''
      }).catch((err) => {
        console.log(err.response)
      })
    },
  }
}
</script>

<style>
#comment-input {
  display: flex;
  width: 40%;
  margin-left: 30%;
}

</style>