<template>
  <div class="carousel-item" :class="{ 'active': index === 0}">
    <!-- :alt="videoData.snippet.title" -->
    <img class="d-block w-100" :src="thumbnail" alt="videoTitle">
  </div>
</template>

<script>
import axios from 'axios'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/videos'


export default {
  name: 'VideoListItem',
  props: {
    video: Object,
    index: Number,
  },
  data: function() {
    return {
      videoData: [],
      videoURI: `https://www.youtube.com/embed/${this.video.key}`,
      thumbnail: '',
    }
  },
  mounted: function () {
    // get VideoSnippet
    // console.log(process.env.VUE_APP_YOUTUBE_API_KEY)
    // console.log(YOUTUBE_API_KEY)
    const params = {
      key: YOUTUBE_API_KEY,
      part: 'snippet',
      id: this.video.key,
    }
    axios({
      method: 'GET',
      url: YOUTUBE_API_URL,
      params: params,
      headers: {
        Authorization: '',
      }        
    }).then((res) => {
      console.log(res.data)
      if (res.data.items) {
        console.log('complete')
        this.videoData = res.data.items
        this.thumbnail = this.videoData[0].snippet.thumbnails.high.url
        // console.log(this.videoData)
        // console.log(this.thumbnail)
        this.$emit('foundVideo')
      }
    }).catch((err) => {
      console.log(err.response)
    })
  }
}
</script>

<style>

</style>