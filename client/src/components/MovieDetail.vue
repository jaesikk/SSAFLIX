<template>
  <div id="MovieDetail" class="container">

    <div id="movie-bg">
      <img id="movie-bg-poster" class="img-fluid" :src="backdropPath" alt="poster">
    <!-- {{movie}} -->
    <h1 class="display-1">{{ movie.title }}</h1>
    </div>
    <hr>
    <div class="container">
      <div class="row">
        <div class="col">
          <img id="movieposter" class="img-fluid rounded" :src="poster" alt="poster">
        </div>
        <div class="col">
          <div id="info" >
            <h4>개봉일 : {{movie.release_date}}</h4>
            <h4>평점 : {{movie.vote_average}}</h4>
          </div>
        <hr>
          <h3>줄거리</h3>
          <br>
          <p class="fs-5"> {{movie.overview}} </p>
        <hr>

        <h3>트레일러</h3>
        <br>
          <div v-show="isFoundVideo" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" data-bs-interval="false">
            <div class="carousel-inner">
              <VideoListItem v-for="(video, index) in videoList" :key="video.key" :video="video" :index="index" @foundVideo="onFoundVideo" />
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
        </div>
      </div>
    </div>
    <hr>

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
</template>

<script>
import axios from 'axios'
import VideoListItem from '@/components/VideoListItem.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
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
      poster: "https://image.tmdb.org/t/p/w500/" + String(this.movie.poster_path),
      backdropPath: '',
      images: [],
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
    }),
    // TMDB에서 backdrops, posters, 추가적인 이미지 GET요청받기
    axios ({
      methods: 'GET',
      url: `https://api.themoviedb.org/3/movie/${this.movie.tmdb_id}/images`,
      params: {
        api_key: TMDB_API_KEY,
        language: "ko-KR",
        include_image_language: "ko,en",
      }
    }).then((res) => {
      console.log(res)
      this.images = res.data
      this.backdropPath = "https://image.tmdb.org/t/p/original/" + String(this.images.backdrops[0].file_path)
      console.log(this.images.backdrops[0].file_path)
    }).catch((err) => {
      console.log(err.response)
    })
  }
}
</script>

<style>
#MovieDetail {
  width: 70%;
}
.px-wide-600 {
  width: 600px;
}
#info {
  text-align: left;
  margin-left: 50px;
}
.fs-5 {
  text-align: left;
}
#movie-bg {
  position: relative;
  overflow: hidden;
  height: 300px;
  /* height: 50%; */
}

#movie-bg-poster{
  position: absolute;
  display: flex;
  overflow: hidden;
  opacity: 0.5;
  z-index: -1;
  /* width: 100%; */
  /* background-image: linear-gradient(); */
  
}
#movieposter {
  /* margin-bottom: 0px 50px; */
  box-shadow: 10px 10px 10px rgba(219, 214, 214, 0.7);
  margin: 50px 0px;
}
</style>