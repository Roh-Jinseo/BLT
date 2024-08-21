<template>
  <div>
    <h3>Article List</h3>
    <div v-if="store.articles.length">
      <ArticleListItem 
        v-for="(article, index) in reversedArticles"
        :key="article.id"
        :article="article"
        :index="index"
      />
    </div>
    <div v-else>글이 존재하지 않습니다.</div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
const reversedArticles = computed(() => [...store.articles].reverse())
</script>