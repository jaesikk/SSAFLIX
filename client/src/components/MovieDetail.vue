<template>
  <div id="MovieDetail">
    <h1>{{ movie.title }}</h1>

    <h2>동영상</h2>
    <div v-show="isFoundVideo" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" data-bs-interval="false">
      <div class="carousel-inner">
        <VideoListItem v-for="(video, index) in videoList" :key="video.key" :video="video" :index="index" @foundVideo="onFoundVideo" />
        <!-- <div class="carousel-item active">
          <img src="" class="d-block w-100" alt="...">
        </div> -->
        <!-- <div class="carousel-item">
          <img src="" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="" class="d-block w-100" alt="...">
        </div> -->
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!-- <div class="video-container">
      <iframe 
        id="ytplayer" 
        type="text/html"
        width="640" height="360"
        :src="videoURI"
        frameborder="0">
      </iframe>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import VideoListItem from '@/components/VideoListItem.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
    movieId: Number,
  },
  components: {
    VideoListItem,
  },
  data: function () {
    return {
      videoList: [],
      videoURI: '',
      isFoundVideo: false,
    }
  },
  methods: {
    onFoundVideo: function () {
      this.isFoundVideo = true
    },
  },
  mounted: function () {
    // console.log(axios.defaults.headers.common['Authorization'])
    axios({
      methods: 'GET',
      url: SERVER_URL + `/movies/${this.movie.id}/videos/`
    }).then((res) => {
      this.videoList = res.data
      // if (this.videoList) {
        // this.videoURI = `https://www.youtube.com/embed/${this.videoList[0].key}`        
        // console.log(this.videoURI)
        // this.isFoundVideo = true
      // }
    }).catch((err) => {
      console.log(err.response)
    })
  }
}
</script>

<style>
.px-wide-600 {
  width: 600px;
}
</style>