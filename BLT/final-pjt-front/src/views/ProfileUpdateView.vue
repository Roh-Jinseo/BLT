<template>
  <div>
    <nav class="nav">
      <RouterLink class="link" :to="{ name: 'ProfileView', params: { username: username } }">프로필</RouterLink>
      <RouterLink class="link" :to="{ name: 'ProfileProductView', params: { username: username } }">가입한 상품 목록</RouterLink>
      <RouterLink class="link" :to="{ name: 'ProfileUpdateView', params: { username: username } }">프로필 수정</RouterLink>
    </nav>
    <div class="profile-container">
      <br>
      <h2 class="small-caps sans-serif">프로필 수정</h2>
      <div>
        <div v-if="img">
          <img :src="img" alt="Profile Picture">
        </div>
        <div v-else>
          <img src="@/assets/mascot.png" alt="Profile Picture" width="100">
        </div>
      </div>
      <form @submit.prevent="changeProfile">
        <div class="profile-info">
          <div class="row">
            <div class="col-6" >Profile Image</div>
            <div class="col-6">
              <input type="file" @change="handleFileChange" id="image" >
              
          </div>
          </div>

          <!-- <label for="image">Profile Image 수정</label>
          <input type="file" @change="handleFileChange" id="image"> -->
          <div class="row">
            <div class="col-6">아이디</div>
            <div class="col-6">{{ username }}</div>
          </div>
          <div class="row">
            <div class="col-6">이름</div>
            <div class="col-6">{{ lastName }} {{ firstName }}</div>
          </div>
          <div class="row">
            <div class="col-6">닉네임</div>
            <div class="col-6"><input type="text" v-model="nickname"></div>
          </div>
          <div class="row">
            <div class="col-6">나이</div>
            <div class="col-6"><input type="number" v-model="age"></div>
          </div>
          <div class="row">
            <div class="col-6">연봉</div>
            <div class="col-6"><input type="number" v-model="salary"></div>
          </div>
          <div class="row">
            <div class="col-6">현재 자산</div>
            <div class="col-6"><input type="number" v-model="currentAsset"></div>
          </div>
          <div class="row">
            <div class="col-6">성별</div>
            <div class="col-6">
              <input type="radio" id="female" name="gender" value="0" v-model.number="gender" />
              <label for="female">여자</label>
              <input type="radio" id="male" name="gender" value="1" v-model.number="gender" />
              <label for="male">남자</label>
            </div>
          </div>
          <div class="row">
            <div class="col-6">이메일</div>
            <div class="col-6"><input type="text" v-model="email"></div>
          </div>
          <div class="row" v-if="financial_products">
            <div class="col-6">가입 상품</div>
            <div class="col-6">{{ financial_products }}</div>
          </div>
          <div v-else>
            가입한 상품이 없습니다.
          </div>
        </div>
        <!-- <button type="submit" class="btn btn-light">프로필 수정</button> -->
        <button type="submit" class="btn btn-outline-dark" >프로필 수정</button>
        <!-- <input type="submit" value="프로필 수정"> -->
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import router from '@/router';

const store = useCounterStore();
const route = useRoute();

const username = ref(store.userInfo.username);
const email = ref(store.userInfo.email);
const firstName = ref(store.userInfo.first_name);
const lastName = ref(store.userInfo.last_name);
const age = ref(store.userInfo.age);
const salary = ref(store.userInfo.salary);
const currentAsset = ref(store.userInfo.currentAsset);
const nickname = ref(store.userInfo.nickname);
const gender = ref(store.userInfo.gender);
const img = ref(store.userInfo.img);
const financial_products = ref(store.userInfo.financial_products);

const editedProfileImg = ref({ image: null });
const handleFileChange = (event) => {
  const file = event.target.files[0];
  editedProfileImg.value.image = file;
};

const changeProfile = () => {
  const formData = new FormData();
  formData.append('username', username.value);
  formData.append('email', email.value);
  formData.append('firstName', firstName.value);
  formData.append('lastName', lastName.value);
  formData.append('age', age.value);
  formData.append('salary', salary.value);
  formData.append('currentAsset', currentAsset.value);
  formData.append('nickname', nickname.value);
  formData.append('gender', gender.value);
  if (editedProfileImg.value.image) {
    formData.append('img', editedProfileImg.value.image);
  }

  axios({
    method: 'put',
    url: `${store.API_URL}/accounts/update/${username.value}/`,
    data: formData,
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data',
    },
  })
    .then((res) => {
      router.push({ name: 'ProfileView', params: { username: username.value } });
      store.getUserInfo();
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
img {
  max-width: 200px;
  height: auto;
}

.nav {
  margin-right: 10px;
  color: skyblue;
  font: small-caps bold 18px/1 sans-serif;
}

.link {
  text-decoration: none;
  color: black;
  margin: 10px;
}

.profile-container {
  background-color: #b2dfdb;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 50rem;
  text-align: center;
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

.row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.col-6 {
  width: 45%;
}
</style>
