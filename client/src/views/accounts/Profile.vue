<template>
  <div>
    <h1>{{ user.username }}'s Profile</h1>
    <span>{{ reviewUser }}</span>
    <!-- {{ review }} -->
    <div>
      <!-- <button @click="onFollow" >{{ isFollow ? '팔로우 취소' : '팔로우'}} </button> -->
    </div>
    <button @click="getUser">정보가져오기</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  props: {
    reviewUser: Number,
    review: Object,
  },
  data: function () {
    return {
      // nowReview: this.review,
      isFollow: false,
      user: [],
    }
  },
  computed: {
    ...mapState(['accounts'])
  },
  methods: {
    onFollow: function() {
      axios ({
        method: 'POST',
        url: SERVER_URL + `/accounts/${this.review.user}/follow/`,
      }).then((res) => {
        console.log(res.data)
        this.isFollow = res.data.isFollow
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
      },
    getUser: function() {
      axios ({
        method: 'GET',
        url: SERVER_URL + `/accounts/${this.review.user}/`,
      }).then((res) => {
        console.log(res.data)
        this.user = res.data
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
  },
  mounted: function () {
    this.getUser()
  }
}
</script>

<style>

</style>