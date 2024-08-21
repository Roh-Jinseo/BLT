<template>
  <div style="background-color: #b2dfdb; height: 50rem;">
    <br>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title small-caps sans-serif" style="text-align: center;">회원가입</h2>
        <hr>
        <form @submit.prevent="signUp">
          <div class="form-group row form-row">
            <label for="username" class="col-sm-6 col-form-label">유저아이디</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="username" id="username">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="password1" class="col-sm-6 col-form-label">비밀번호</label>
            <div class="col-sm-6">
              <input type="password" class="form-control gray-input" v-model.trim="password1" id="password1">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="password2" class="col-sm-6 col-form-label">비밀번호 검증</label>
            <div class="col-sm-6">
              <input type="password" class="form-control gray-input" v-model.trim="password2" id="password2">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="email" class="col-sm-6 col-form-label">이메일</label>
            <div class="col-sm-6">
              <input type="email" class="form-control gray-input" v-model.trim="email" id="email">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="age" class="col-sm-6 col-form-label">나이</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="age" id="age">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="salary" class="col-sm-6 col-form-label">연봉</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="salary" id="salary">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="currentAsset" class="col-sm-6 col-form-label">현재 자산</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="currentAsset" id="currentAsset">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="lastName" class="col-sm-6 col-form-label">성</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="lastName" id="lastName">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="firstName" class="col-sm-6 col-form-label">이름</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="firstName" id="firstName">
            </div>
          </div>

          <div class="form-group row form-row">
            <label for="nickname" class="col-sm-6 col-form-label">닉네임</label>
            <div class="col-sm-6">
              <input type="text" class="form-control gray-input" v-model.trim="nickname" id="nickname">
            </div>
          </div>

          <div class="form-group row form-row">
            <label class="col-sm-6 col-form-label">성별</label>
            <div class="col-sm-6">
              <input type="radio" id="genderone" value="0" v-model.number="gender" />
              <label for="genderone">여자</label>
              <input type="radio" id="gendertwo" value="1" v-model.number="gender" />
              <label for="gendertwo">남자</label>
            </div>
          </div>

          <!-- <br> -->
          <div class="form-group row" style="text-align: right;">
            <div class="col-sm-12">
              <button type="submit" class="btn btn-outline-dark">회원가입</button>
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
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const age = ref(null)
const salary = ref(null)
const currentAsset = ref(null)
const firstName = ref(null)
const lastName = ref(null)
const gender = ref(null)
const nickname = ref(null)

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    age: age.value,
    salary: salary.value,
    currentAsset: currentAsset.value,
    firstName: firstName.value,
    lastName: lastName.value,
    gender: gender.value,
    nickname: nickname.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
.card {
  width: 30rem;
  margin: auto;
  margin-top: 2rem;
  background-color: white;
}

.card-body {
  padding: 2rem;
}

.form-row {
  margin-bottom: 1rem; /* Adjust the margin value as needed */
}

.gray-input {
  /* background-color: #d3d3d3;  */
}


</style>
