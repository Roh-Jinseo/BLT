<template>
  <div>
    <h5>{{ store.articles.length-index }}번째 게시글</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>

    <RouterLink 
      :to="{ name: 'ArticleDetailView', params: { id: article.id }}" class="btn btn-outline-dark">
      [DETAIL]
    </RouterLink>


    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

defineProps({
  article: Object,
  index:Number
})
</script>
