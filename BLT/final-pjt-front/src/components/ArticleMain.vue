<template>
  
  <div class="container my-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h3>자유 게시판</h3>
      <RouterLink :to="{name:'ArticleView'}" class="btn btn-outline-dark">상세보기</RouterLink>
    </div>
    <div v-if="reversedArticles.length">
      <table class="table table-hover">
        <thead class="thead-light">
          <tr>
            <th></th>
            <th>제목</th>
            <th>작성자</th>
            <th>내용</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="(article, index) in reversedArticles" 
            :key="article.id" 
            class="article-row"
            @click="viewArticle(article.id)"
          >   
            <td>{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.user.nickname }}</td>
            <td>{{ article.content }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else role="alert">글이 존재하지 않습니다.</div>
    <!-- <div v-else class="alert alert-warning" role="alert">글이 존재하지 않습니다.</div> -->
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const reversedArticles = computed(() => [...store.articles].reverse())

onMounted(() => {
  store.getArticles()
})

const viewArticle = (articleId) => {
  router.push({ name: 'ArticleView', params: { id: articleId } })
}
</script>

<style scoped>
.article-row {
  cursor: pointer;
  transition: background-color 0.2s;
}

.article-row:hover {
  background-color: #fdfdfd;
}
</style>
