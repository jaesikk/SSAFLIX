<template>
  <div>
    <h1>Profile</h1>
    <span>{{ reviewUser }}</span>
    {{ review }}
    <div>
      <!-- <button @click="onFollow" >{{ isFollow ? '팔로우 취소' : '팔로우'}} </button> -->
    </div>
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
  // data: function () {
  //   nowReview: this.review,
  //   isFollow: '',
  // },
  computed: {
    ...mapState(['accounts'])
  },
  onFollow: function() {
    axios ({
      method: 'POST',
      url: SERVER_URL + `/accounts/${this.nowReview.user}/follow/`,
    }).then((res) => {
      console.log(res.data)
      this.isFollow = res.data.isFollow
    }).catch((err) => {
      console.log(err.response)
      alert(err.response.data.error)
    })
  },
}
</script>

<style>

</style>