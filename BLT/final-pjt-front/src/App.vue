<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><RouterLink :to="{ name: 'MainView' }">BLT</RouterLink></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink :to="{ name: 'MainView' }">Main</RouterLink> |
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ProductView' }">금융상품</RouterLink> |
            </li>        
            <li class="nav-item">
              <RouterLink :to="{ name: 'ArticleView' }">자유게시판</RouterLink> |
            </li>        
            <li class="nav-item">
              <RouterLink :to="{ name: 'ExchangeRatesView' }">환율 계산기</RouterLink>|
            </li>
            <li class="nav-item"> 
              <RouterLink :to="{ name: 'MapView' }">은행 지도</RouterLink>|
            </li>
            <li class="nav-item"> 
              <RouterLink :to="{ name: 'AboutUsView' }">About us</RouterLink>
            </li>
          </ul>
          
          <ul class="navbar-nav ms-3 mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle d-flex align-items-center" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">

                
                
                <div  v-if="store.saveUsername"> <!--로그인 시-->
                  <span class="img-area me-2">
                    <span v-if="img">
                      <img :src="img" alt="Profile Picture"  width="45" height="45" class="d-inline-block align-text-center">
                    </span>
                    <span v-else>
                      <img src="@/assets/mascot.png" alt="BLT Profile Picture"  width="45" height="45" class="d-inline-block align-text-center">
                    </span>
                    <!-- <img :src="img" alt="Profile Picture" width="45" height="45" class="d-inline-block align-text-center"> -->
                  </span>
                  <!-- <span >안녕하세요, <br>{{store.saveUsername}}님</span> -->
                  <span >{{store.saveUsername}}님, 안녕하세요</span>
                </div>
                <div v-else> <!--비로그인 시-->
                  <span class="img-area me-2"><img src="@/assets/mascot.png" alt="Logo" width="45" height="45" class="d-inline-block align-text-center"></span>
                  <!-- <span >안녕하세요, <br>익명님</span> -->
                  <span >안녕하세요, 익명님</span>
                </div>


              </a>
              <ul class="dropdown-menu">
                <div v-if="!(store.isLogin)">
                  <li><RouterLink class="dropdown-item" :to="{ name: 'SignUpView' }">회원가입</RouterLink></li>
                  <li><RouterLink class="dropdown-item" :to="{ name: 'LogInView' }">로그인</RouterLink></li>
                </div>
                <div v-else>
                  <li><RouterLink class="dropdown-item" :to="{ name: 'ProfileView', params: { username: username } }">프로필</RouterLink></li>
                  <li><RouterLink class="dropdown-item" :to="{ name: 'LogOutView' }">로그아웃</RouterLink></li>
                </div>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <main>
  <RouterView />
  <!-- <ChatBot /> -->
  </main>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref, computed } from 'vue'
import ChatBot from './components/ChatBot.vue'

const store = useCounterStore()
const username = computed(() => store.saveUsername)
const img = computed(() => store.userInfo?.img);


</script>

<style scoped>


main {
  font-family: 'WooridaumB';
  background-color: #B2DFDB;
  height: 50rem;
}

.navbar {
  background-color: transparent; /* 배경을 투명하게 설정 */
  border-bottom: 1px solid #e9ecef;
}

.dropdown-item {
  text-decoration: none;
  color: cadetblue;
  /* font: small-caps bold 18px/1 sans-serif; */
}

.nav-item > a {
  margin-right: 10px;
  text-decoration: none;
  color: black;
  font-weight: bold;
  /* font: small-caps bold 18px/1 sans-serif; */
}

.navbar-brand > a {
  margin-right: 1px;
  text-decoration: none;
  color: cadetblue;
  font: small-caps bold 18px/1 sans-serif;
  font-size: 30px;
}

.navbar-nav .nav-item.dropdown .dropdown-menu {
  left: auto;
  right: 0;
}

</style>
