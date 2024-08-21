<template>
  <nav class="nav">
    <RouterLink class="link" :to="{ name: 'ProfileView', params: { username: username } }">프로필</RouterLink>
    <RouterLink class="link" :to="{ name: 'ProfileProductView', params: { username: username } }">가입한 상품 목록</RouterLink>
    <RouterLink class="link" :to="{ name: 'ProfileUpdateView', params: { username: username } }">프로필 수정</RouterLink>
  </nav>
  <div class="profile-container">
    <br>
    <h2 class="small-caps sans-serif">프로필 페이지</h2>
    <br>
    <div class="profile-content">
      <div v-if="img">
        <img :src="img" alt="Profile Picture">
      </div>
      <div v-else>
        <img src="@/assets/mascot.png" alt="BLT Profile Picture" width="100">
      </div>
      <div class="profile-info">
        <div class="row">
          <div class="col-6">아이디</div>
          <div class="col-6">{{ username }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">이름</div>
          <div class="col-6">{{ lastName }} {{ firstName }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">닉네임</div>
          <div class="col-6">{{ nickname }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">나이</div>
          <div class="col-6">{{ age }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">연봉</div>
          <div class="col-6">{{ salary }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">현재 자산</div>
          <div class="col-6">{{ currentAsset }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">성별</div>
          <div class="col-6">{{ gender }}</div>
        </div>
        <br>
        <div class="row">
          <div class="col-6">이메일</div>
          <div class="col-6">{{ email }}</div>
        </div>
        <br>
        <div class="row" v-if="financial_products">
          <div class="col-6">가입 상품</div>
          <div class="col-6">{{ financial_products }}</div>
        </div>
        <div class="row" v-else>
          <div class="col-12">가입한 상품이 없습니다.</div>
        </div>
        <br>
        <div class="row">
            <button @click="store.unregister(username)" class="btn btn-outline-dark w-50">회원탈퇴</button>
        </div>
        <br>
      </div>
    </div>
  </div>
  <button @click="store.unregister(username)" class="btn btn-outline-dark">회원탈퇴</button>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const route = useRoute();
const username = computed(() => store.userInfo?.username);
const email = computed(() => store.userInfo?.email);
const firstName = computed(() => store.userInfo?.first_name);
const lastName = computed(() => store.userInfo?.last_name);
const age = computed(() => store.userInfo?.age);
const salary = computed(() => store.userInfo?.salary);
const currentAsset = computed(() => store.userInfo?.currentAsset);
const nickname = computed(() => store.userInfo?.nickname);
const gender = computed(() => store.userInfo?.gender);
const img = computed(() => store.userInfo?.img);
const financial_products = computed(() => store.userInfo?.financial_products);
</script>

<style scoped>

nav {
  background-color: #ffffff;
}
.profile-container {
  background-color: #B2DFDB;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 50rem;
  text-align: center;
}

.profile-content {
  display: flex;
  margin-left: 20px;
  padding-left: 20px;
}

.profile-info {
  margin-top: 20px;
  margin-left: 50px;
  padding-left: 20px;
  flex: 1;
  text-align: start;
  font: small-caps bold 18px/1 sans-serif;
  color: #010125;
}

img {
  max-width: 500px;
  width: 200px;
  height: auto;
  border-radius: 50%;
}

.link {
  text-decoration: none;
  color: black;
  margin: 10px;
}

.nav {
  margin-right: 10px;
  color: skyblue;
  font: small-caps bold 18px/1 sans-serif;
}
</style>
