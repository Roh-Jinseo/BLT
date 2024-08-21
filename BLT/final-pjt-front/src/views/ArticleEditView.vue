<template>
  <div class="container">
    <h1 class="mt-5 mb-4">게시글 수정</h1>
    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="mb-3 w-75">
        <label for="title" class="form-label">제목</label>
        <input type="text" class="form-control" v-model.trim="editedArticle.title" id="title">
      </div>
      <div class="mb-3 w-75">
        <label for="content" class="form-label">내용</label>
        <textarea class="form-control" v-model.trim="editedArticle.content" id="content" rows="5"></textarea>
      </div>
      <div class="mb-3 w-25">
        <div>
        <!-- <label for="image" class="form-label">이미지 {{ existingImage ? '바꾸기' : '업로드' }}</label> -->
        <input v-if="!existingImage" class="form-control" type="file" @change="handleFileChange" id="image">
        <input v-else class="form-control" type="file" @change="handleFileChange" id="image" style="display: none;">
        <button @click.prevent="existingImage ? handleFileInputClick() : null" type="button" class="btn btn-outline-dark mt-2">
          {{ existingImage ? '이미지 바꾸기' : '이미지 업로드' }}
        </button>
      </div>
      <div>
        <span v-if="existingImage" class="ml-2">현재 이미지: {{ editedArticle.image.name || editedArticle.image }}</span>
      </div>
      </div>
      <button type="submit" class="btn btn-outline-dark">수정 완료</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const editedArticle = ref({
  title: '',
  content: '',
  image: null
})
let existingImage = false

const handleFileChange = (event) => {
  const file = event.target.files[0]
  editedArticle.value.image = file
}

const handleFileInputClick = () => {
  if (fileInput.value) {
    fileInput.value.click();
  }
}

const loadArticle = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(response => {
      editedArticle.value.title = response.data.title
      editedArticle.value.content = response.data.content
      if (response.data.image) {
        existingImage = true
        editedArticle.value.image = response.data.image
      }
    })
    .catch(error => {
      console.log(error)
    })
}

const submitForm = () => {
  const formData = new FormData()
  formData.append('title', editedArticle.value.title)
  formData.append('content', editedArticle.value.content)
  // 만일 사진이 수정이 되었을 경우에만 넘겨주기로 함
  if (editedArticle.value.image) {
    formData.append('image', editedArticle.value.image)
  }

  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    data: formData,
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then((response) => {
      router.push({ name: 'ArticleView', params: { id: route.params.id } })
    })
    .catch((error) => {
      console.log(error)
    })
}

onMounted(() => {
  loadArticle()
})
</script>

<style>

</style>
