import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'
import Profile from '../views/accounts/Profile.vue'
import Community from '../views/community/Community.vue'
import CreateReview from '../views/community/CreateReview.vue'
import UpdateReview from '../views/community/UpdateReview.vue'
import ReviewDetail from '../views/community/ReviewDetail.vue'
import Recommend from '../views/movies/Recommend.vue'
import MovieDetail from '@/components/MovieDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/Signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/:reviewUser/Profile',
    name: 'Profile',
    component: Profile,
    // props: route => ({
    //   reviewUser: Number(route.params.review),
    //   review: route.params.review,
    // }),
    props: true,
  },
  {
    path: '/community/Community',
    name: 'Community',
    component: Community
  },
  {
    path: '/movies/Recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/community/CreateReview',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/community/:reviewId/ReviewDetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props: route => ({
      review: route.params.review,
      reviewId: route.params.review,
    }),
  },
  {
    path: '/community/:reviewId/UpdateReview',
    name: 'UpdateReview',
    component: UpdateReview,
    props: route => ({
      review: route.params.review,
      reviewId: route.params.review,
    }),
  },
  {
    path: '/movies/:movieId/',
    name: 'MovieDetail',
    component: MovieDetail,
    // props: route => ({
    //   movie: route.params.movie,
    //   movieId: route.params.movie,
    // }),
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
