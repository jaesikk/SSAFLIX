<template>
  <li>
    <p>{{ comment }}</p>
  </li>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateComment',
  props: {
    review: {
      type: Object,
    }
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
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style>

</style>