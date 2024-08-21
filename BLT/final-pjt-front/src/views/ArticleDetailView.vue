<template>
  <div class="container mt-5">
    <h1 class="mb-4">DetailView</h1>
    <div class="card">
      <div class="card-body">
        <!-- 게시물 -->
        <div v-if="article">
          <p class="mb-1">
            <strong>작성일:</strong> {{ article.created_at }} <br />
            <strong>작성자:</strong> {{ article.user.nickname }}
          </p>
          <p v-if="article.created_at !== article.updated_at" class="mb-1"><strong>수정일:</strong> {{ article.updated_at }}</p>
          <h5 class="card-title">{{ article.title }}</h5>
          <p class="card-text">{{ article.content }}</p>
          <div v-if="article.image" class="mb-3">
            <img :src="getImageUrl(article.image)" alt="article image" class="img-fluid">
          </div>
          <div class="mb-3">
            <button
              @click="toggleLike"
              class="btn btn-outline-dark btn-sm">
              <i  v-if="!isLiked" class="fa-regular fa-heart" style="color: red;"></i>
              <i v-else class="fa-solid fa-heart" style="color: red;"></i>
            </button>

            <!-- <button @click="toggleLike" class="btn btn-outline-dark btn-sm">
              {{ isLiked ? '좋아요 취소' : '좋아요' }}
            </button> -->
            &nbsp;
            <span class="ml-2">좋아요 수: {{ article.likes_count }}</span>
          </div>
          <div v-if="isAuthor" class="mb-3">
            <button @click="editArticle" class="btn btn-outline-dark btn-sm mr-2">글 수정</button> &nbsp;
            <button @click="store.deleteArticle(article.id)" class="btn btn-danger btn-sm">글 삭제</button>
          </div>
          <!-- 댓글 -->
          <h5 v-if="store.comments.length" class="mt-4">Comments ({{ store.comments.length }})</h5>
          <ul class="list-group">
            <li v-for="comment in store.comments" :key="comment.id" class="list-group-item">
              <Comment :comment="comment"/>
            </li>
          </ul>
          <form @submit.prevent="submitComment" class="mt-3">
            <div class="form-group">
              <textarea v-model="newComment" class="form-control" placeholder="댓글을 작성하시오"></textarea>
            </div>
            <button type="submit" class="btn btn-outline-dark btn-sm">작성하기</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import Comment from '@/components/Comment.vue'


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const newComment = ref('')
const isLiked = ref(false)

const isAuthor = computed(() => {
  return article.value && article.value.user.username === store.saveUsername
})

const getImageUrl = (imagePath) => {
  return `${store.API_URL}${imagePath}`
}

const submitComment = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comment-create/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: newComment.value
    }
  })
    .then((response) => {
      store.comments.push(response.data)
      newComment.value = ''
    })
    .catch((error) => {
      console.log(error)
    })
}

const editArticle = function() {
  router.push({ name: 'ArticleEditView', params: { id: article.value.id } })
}


// 게시물 - 좋아요 기능
const checkIfLiked = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/likes/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      isLiked.value = response.data.is_liked
    })
    .catch((error) => {
      console.log(error)
    })
}

const toggleLike = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      isLiked.value = !isLiked.value
      if (isLiked.value) {
        article.value.likes_count += 1
      } else {
        article.value.likes_count -= 1
      }
    })
    .catch((error) => {
      console.log(error)
    })
}



onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      article.value = response.data
      checkIfLiked()
    })
    .catch((error) => {
      console.log(error)
    })

  store.getComments(route.params.id)
})
</script>

<style>
/* Add your styles here */
</style>
