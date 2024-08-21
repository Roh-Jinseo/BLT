<template>
  <div style="height: 50rem; background-color: #b2dfdb;">
    <br>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title small-caps sans-serif" style="text-align: center;">로그인</h2>
        <hr>
        <form @submit.prevent="logIn">      
          <div class="form-group row form-row">
            <label for="username" class="col-sm-6 col-form-label">username</label>
            <div class="col-sm-6">
              <input type="text" class="form-control" v-model.trim="username" id="username">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="password" class="col-sm-6 col-form-label">password</label>
            <div class="col-sm-6">
              <input type="password" class="form-control" v-model.trim="password" id="password">
            </div>
          </div>
          
          <br>
          <div class="form-group row" style="text-align: right;">
            <div class="col-sm-12">
              <button type="submit" class="btn btn-outline-dark">Login</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.card {
  width: 30rem;
  margin: auto;
  margin-top: 2rem;
}

.card-body {
  padding: 2rem;
}

.form-row {
  margin-bottom: 1rem; /* Adjust the margin value as needed */
}
</style>
