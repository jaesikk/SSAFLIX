import axios from "axios"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

const userStore = {
  namespaced: true,
  state: {
    accounts: {
      userId: '',
      username: '',
      point: 0,
    },
    token: '',
    isLogin: false,
  },
  mutations: {
    ADD_USER: function (state, data) {
      state.accounts.userId = data.user.id
      state.accounts.username = data.user.username
      state.accounts.point = data.user.point
      state.isLogin = true
      state.token = data.token
    },
    DELETE_USER: function (state) {
      state.accounts.userId = ''
      state.accounts.username = ''
      state.accounts.point = 0
      state.isLogin = false
      state.token = ''
    }
  },
  actions: {
    // credetials에 담아서 ADD_USER를 동작시킨다.
    loginUser: function (context, credentials) {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: credentials,
      }).then((res) => {
        context.commit('ADD_USER', res.data)
        // axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        console.log(res.data)
        axios.defaults.headers.common['Authorization'] = `JWT ${context.state.token}`
        localStorage.setItem('jwt', res.data.token)
      })
    },
    logoutUser: function (context) {
      context.commit('DELETE_USER')
      localStorage.removeItem('jwt')
      // console.log(this.state.accounts)
    }
  },
}

export default userStore