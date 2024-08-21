<template>
  <div class="card-body">
    <h3 class="card-title">{{ deposit.fin_prdt_nm }}</h3>
    <p class="card-text"><strong>은행:</strong> {{ deposit.kor_co_nm }}</p>
    <!-- <p class="card-text"><strong>가입방법:</strong> {{ deposit.join_way }}</p>
    <p class="card-text"><strong>특이사항:</strong> {{ deposit.etc_note }}</p> -->
    
    <div v-if="deposit.options && deposit.options.length > 0">
      <h5 class="mt-4">옵션 목록:</h5>
      <ul class="list-group">
        <li v-for="option in deposit.options" :key="option.id" class="list-group-item">
          <p><strong>저장 기간:</strong> {{ option.save_trm }}개월</p>
          <p><strong>금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
          <p><strong>금리:</strong> {{ option.intr_rate }}%</p>
          <p><strong>최고우대금리:</strong> {{ option.intr_rate2 }}%</p>
        </li>
      </ul>
    </div>
    
    <RouterLink :to="{name:'ProductDepositDetailView', params:{fin: deposit.fin_prdt_cd}}" class="btn btn-dark">
      상세보기
    </RouterLink> 
  
  </div>
</template>

<script setup>
import { RouterLink,RouterView } from 'vue-router'
import { useProductStore } from '@/stores/product';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';


const store = useProductStore()
const route = useRoute

defineProps({
  deposit:Object
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