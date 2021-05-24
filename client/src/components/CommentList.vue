<template>
  <li>
    <p>ddd</p>
  </li>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentList',
  props: {
    review: {
      type: Object,
    },
    comments: [],
  },
  methods: {

  },
}
</script>

<style>

</style>