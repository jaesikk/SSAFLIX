<template>
  <div class="container">
    <h1>{{ user.username }}'s Profile</h1>
    <!-- {{ review }} -->
    <div class="d-flex justify-content-between">
      <button class="btn btn-danger" @click="onFollow"><i class= "fa-heart" :class="[ isFollow ? 'fas': 'far']"></i></button>
      <span>팔로우: {{ user.followData.followingCnt }} | 팔로워: {{ user.followData.followerCnt }} | 포인트: {{ user.point }}</span>
    </div>
    <hr>
    <!-- <button @click="getUser">정보가져오기</button> -->
  </div>
</template>

<script>
// import { mapState } from 'vuex'
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
      nowReview: this.review,
      isFollow: '',
      user: [],
    }
  },
  // computed: {
  //   ...mapState(['accounts'])
  // },
  methods: {
    onFollow: function() {
      axios ({
        method: 'POST',
        url: SERVER_URL + `/accounts/${this.reviewUser}/follow/`,
      }).then((res) => {
        console.log(res.data)
        this.isFollow = res.data.isFollow
        // 팔로우 데이터를 보내고 getUser를 통해 갱신시켜 팔로우, 팔로워 수를 갱신
        this.getUser()
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
    getUser: function() {
      axios ({
        method: 'GET',
        url: SERVER_URL + `/accounts/${this.reviewUser}/`,
      }).then((res) => {
        console.log(res)
        this.user = res.data
      }).catch((err) => {
        console.log(err.response)
        alert(err.response.data.error)
      })
    },
  },
  mounted: function () {
    this.getUser()
    console.log(this.getUser)
  },
}
</script>

<style>

</style>