<template>
  <div>
    <h1>{{ reviewTitle}}</h1>
    <router-link :to="{ name: 'Community' }" class="d-flex justify-content-end ml-3">back</router-link>
    <hr>
    <h2>후기</h2>
    <p>{{ reviewContent }}</p>
    <button @click="checkId">버튼</button>
    <hr>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ReviewDetail',
  props: {
    reviewTitle: String,
    reviewContent: String,
  },
  data: function () {
    return {

    }
  },
  computed: {
    ...mapState(['accounts'])
  },
  methods: {
    checkId: function () {
      console.log(this.$store.state.accounts)
    },
  }
}
</script>

<style>

</style>