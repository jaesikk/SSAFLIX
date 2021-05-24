<template>
  <div>
    <input type="text" v-model="comment" @keyup.enter="getComments">
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
  }
}
</script>

<style>

</style>