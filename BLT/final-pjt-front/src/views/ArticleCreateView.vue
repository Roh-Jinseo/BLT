<template>
  <div class="container">
    <h1 class="mt-5 mb-4">게시글 작성</h1>
    <form @submit.prevent="createArticle" enctype="multipart/form-data">
      <div class="mb-3 w-75">
        <label for="title" class="form-label">제목</label>
        <input type="text" class="form-control" v-model.trim="title" id="title">
      </div>
      <div class="mb-3 w-75">
        <label for="content" class="form-label">내용</label>
        <textarea class="form-control" v-model.trim="content" id="content" rows="5"></textarea>
      </div>
      <div class="mb-3 w-25">
        <label for="image" class="form-label">이미지 업로드</label>
        <input class="form-control" type="file" @change="onFileChange" id="image">
      </div>
      <button type="submit" class="btn btn-outline-dark">작성 완료</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref('')
const content = ref('')
const image = ref(null)
const router = useRouter()

const onFileChange = function (event) {
  image.value = event.target.files[0]
}

const createArticle = function () {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  if (image.value) {
    formData.append('image', image.value)
  }

  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: formData,
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then((response) => {
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style>

</style>
