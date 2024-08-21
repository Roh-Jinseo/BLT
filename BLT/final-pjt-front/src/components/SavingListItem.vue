<template>
    <div class="card-body">
      <h3 class="card-title">{{ saving.fin_prdt_nm }}</h3>
      <p class="card-text"><strong>은행:</strong> {{ saving.kor_co_nm }}</p>
      <!-- <p class="card-text"><strong>가입방법:</strong> {{ saving.join_way }}</p> -->
      <!-- <p class="card-text"><strong>특이사항:</strong> {{ saving.etc_note }}</p> -->
  
      <div v-if="saving.options && saving.options.length > 0">
        <h5 class="mt-4">옵션 목록:</h5>
        <ul class="list-group">
          <li v-for="option in saving.options" :key="option.id" class="list-group-item">
            <p><strong>저장 기간:</strong> {{ option.save_trm }}개월</p>
            <p><strong>금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
            <p><strong>금리:</strong> {{ option.intr_rate }}%</p>
            <p><strong>최고우대금리:</strong> {{ option.intr_rate2 }}%</p>
          </li>
        </ul>
      </div>
  
      <RouterLink :to="{ name: 'ProductSavingDetailView', params: { fin: saving.fin_prdt_cd } }" class="btn btn-dark mt-4">
        상세보기
      </RouterLink>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  defineProps({
    saving: Object
  })
  </script>
  
  <style scoped>
  .list-group-item{
  font-size: 13px;
}
 .btn{
  font-size: 15px;
}
  </style>
  