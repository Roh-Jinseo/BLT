<template>
  <div class="outer-container">

    <div class="container">
      <!-- 첫 번째 줄: PredictProduct와 ExchangeMain -->
      <div class="row">
        <div class="col-md-8 product">
          <PredictProduct />
        </div>
        <div class="col-md-4">
          <ExchangeMain />
        </div>
      </div>
    </div>

    <!-- 두 번째 줄: 게시물 목록 -->
    <div class="container mt-4">
      <div class="row">
        <div class="col">
          <ArticleMain />
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import PredictProduct from '@/components/PredictProduct.vue'
import ExchangeMain from '@/components/ExchangeMain.vue'
import ArticleMain from '@/components/ArticleMain.vue'
import { useExchangerStore } from '@/stores/exchanger'
import { computed, onMounted } from 'vue'

const exchangerStore = useExchangerStore()
</script>

<style scoped>

.outer-container {
  padding: 20px;
  /* margin-bottom: 20px; */
}

/* 구분선 스타일 */
.row + .container {
  border-bottom: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 20px;
}

.product {
  border-right: 1px solid #042327; /* ProductList와 PredictProduct 사이에 구분선 추가 */
}

.container {
  background-color: #f7feff;
  padding: 30px;
}

/* 카드 스타일 */

</style>
