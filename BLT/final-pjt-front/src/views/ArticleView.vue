<template>
  <div class="outer-container">
    <div class="container">
      <h3>Article List</h3>
      <div v-if="store.articles.length">
        <table class="table">
          <thead>
            <tr>
              <th></th>
              <th>Title</th>
              <th>Content</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(article, index) in paginatedArticles" :key="article.id">
              <td>{{ (currentPage - 1) * pageSize + index + 1 }}</td>
              <td>{{ article.title }}</td>
              <td>{{ article.content.slice(0, 20) }}{{ article.content.length > 20 ? '...' : '' }}</td>
              <td>
                <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}" class="btn btn-outline-dark btn-sm">Detail</RouterLink>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>글이 존재하지 않습니다.</div>

      <!-- Pagination -->

      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center mt-4">
          <li class="page-item" :class="{ 'disabled': currentPage === 1 }">
            <button class="page-link" @click="currentPage > 1 ? goToPage(currentPage - 1) : ''" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </button>
          </li>
          <li class="page-item" v-for="page in totalPages" :key="page" :class="{ 'active': page === currentPage }">
            <button class="page-link" @click="goToPage(page)">{{ page }}</button>
          </li>
          <li class="page-item" :class="{ 'disabled': currentPage === totalPages }">
            <button class="page-link " @click="currentPage < totalPages ? goToPage(currentPage + 1) : ''" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </button>
          </li>
        </ul>
      </nav>

      <!-- CREATE Button -->
      <div class="create-button">
        <RouterLink :to="{ name: 'ArticleCreateView' }" class="btn btn-outline-dark">
          CREATE
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref,onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

const pageSize = 10; // 한 페이지에 보여줄 게시글 수
const currentPage = ref(1);

const paginatedArticles = computed(() => {
  const startIndex = (currentPage.value - 1) * pageSize;
  return store.articles.slice(startIndex, startIndex + pageSize);
});

const totalPages = computed(() => Math.ceil(store.articles.length / pageSize));

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}
onMounted(()=>{
  store.getArticles()
})

</script>
