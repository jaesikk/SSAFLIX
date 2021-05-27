<template>

    <div class="carousel-item" :class="{'active': index === 0}">
      <!-- Button trigger modal -->
      <!-- :alt="videoData.snippet.title" -->
      <button type="button" class="border-0 p-0" data-bs-toggle="modal" :data-bs-target="'#videoModal'+this.index">
        <img class="d-block w-100" :src="thumbnail" alt="videoTitle">
      </button>
      <!-- Modal -->
      <div class="modal fade" :id="'videoModal'+this.index" data-bs-backdrop="static" tabindex="-1" :aria-labelled-by="'videoModalLabel'+this.index" aria-hidden="true">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" :id="'videoModalLabel'+this.index">{{ videoData[0].snippet.title }}</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" @click="stopVideo"  aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="video-container">
                  <!-- id="ytplayer-'+this.index"  -->
                <iframe 
                  :id="'ytplayer-'+this.index" 
                  type="text/html"
                  :src="videoURI"
                  frameborder="0">
                </iframe>
              </div>
            </div>
          </div>
        </div>
      </div>
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
      videoURI: '',
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
        this.videoURI = `https://www.youtube.com/embed/${this.video.key}`
        // console.log(this.videoData)
        // console.log(this.thumbnail)
        this.$emit('foundVideo')
      }
    }).catch((err) => {
      console.log(err.response)
    })
  },
  methods: {
    stopVideo: function () {
      const st = document.getElementById('ytplayer-'+this.index)
      st.setAttribute('src', this.videoURI)
    }
  }
}
</script>

<style>
/* iframe을 container를 기준으로 위치를 지정 */
/* 유튜브 비디오 비율을 맞추기 위한 높이 설정 */
.video-container {
  position: relative;   
  padding-top: 56.25%;  
}
/* container를 기준으로 위치를 지정*/
/* container의 가장 위쪽으로 위치를 지정 */
.video-container > iframe {
  position: absolute;   
  top: 0;               
  left: 0;
  width: 100%;
  height: 100%;
}
</style>