<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateReview' }" class="navbar-brand">게시글 생성</router-link>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        {{ review.title }}
      </li>
    </ul>
    <CommunityDetail v-for="review in reviews" :key="review.pk" :review="review" />
  </div>
</template>

<script>
import axios from 'axios'
import CommunityDetail from '@/components/CommunityDetail.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Community',
  component: {
    CommunityDetail,
  },
  data: function () {
    return {
      reviews: [],
    }
  },
  methods: {
    getReviews: async function (){
      const res = await axios({
        method: 'GET',
        url: SERVER_URL + '/coummunity/create/'
      })
      this.reviews = res.data
    },

  }
}
</script>

<style>

</style>