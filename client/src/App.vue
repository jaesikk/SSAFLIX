<template>
  <div id="app">
    <div id="nav">
       <!-- nav bar -->
      <nav class="navbar navbar-expand-lg navbar-dark border rounded-pill border-light">
        <div class="container">
          <router-link to="/" class="navbar-brand">Home</router-link> |
          <router-link :to="{ name: 'Recommend' }" class="nav-item">Recommend</router-link> |
          <router-link :to="{ name: 'Community' }">Community</router-link> |
          <router-link :to="{ name: 'Login' }">Login</router-link> |
          <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        </div>
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
