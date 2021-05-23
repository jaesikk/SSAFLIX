<template>
  <div>
    <h1>{{ reviewTitle}}</h1>
    <router-link :to="{ name: 'Community' }" class="d-flex justify-content-end ml-3">back</router-link>
    <hr>
    <h2>후기</h2>
    <p>{{ reviewContent }}</p>
    <hr>

  </div>
</template>

<script>
export default {
  name: 'ReviewDetail',
  props: {
    reviewTitle: String,
    reviewContent: String,
  },
}
</script>

<style>

</style>