<template>
  <div>
    <input type="text" v-model="comment" @keyup.enter="createComment">
    <p>{{ review }}</p>
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
    createComment: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + `/community/${this.review.id}/comments/`,
        data: this.comment,
        // headers: {
        //   Authorization: `JWT ${localStorage.getItem('jwt')}`
        // }        
      }).then((res) => {
        console.log(res)
        this.$router.push({ name: 'Community' })

      }).catch((err) => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style>

</style>