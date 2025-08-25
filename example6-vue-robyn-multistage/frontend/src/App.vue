<template>
  <div class="container">
    <div class="title">Vue 3 + Robyn + Multistage Docker Build Extension</div>

    <div class="description">The following button performs a GET request to the backend:</div>
    <div>
      <button class="button" @click="doRequest">Click me</button>
    </div>
    <div>{{ response }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      response: ''
    }
  },
  methods: {
    async doRequest() {
      const answer = await axios.get('/hello')
      this.response = answer.data
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding-top: 20px;
}

.title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 20px;
}

.description {
  font-size: 18px;
  margin-bottom: 20px;
  align-self: flex-start;
}

.button {
  font-size: 15px;
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  align-items: center;
}
</style>
