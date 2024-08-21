<template>
  <!-- <div class="mt-4"></div> -->
  <div class="outer-container">
  <div class="container mt-4">
    <h2 class="mb-4">원하는 상품을 선택해주세요</h2>
    <div class="form-check form-check-inline">
      <!-- class="btn btn-primary" -->
      <input class="form-check-input" type="checkbox" id="deposit" value="deposit" v-model="selectedOptions">
      <label class="form-check-label" for="deposit">예금</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="saving" value="saving" v-model="selectedOptions">
      <label class="form-check-label" for="saving">적금</label>
    </div>

    <div class="mt-4">
      <h4>은행 선택</h4>
      <select v-model="selectedKorCoName" class="form-select">
        <option value="">모든 은행</option>
        <option v-for="korCoName in korCoNames" :key="korCoName" :value="korCoName">{{ korCoName }}</option>
      </select>
    </div>

    <div class="mt-4">
      <h4>계약 기간 선택</h4>
      <select v-model="selectedSaveTerm" class="form-select">
        <option value="0">전체</option>
        <option v-for="term in saveTrm" :key="term" :value="term">{{ term }} 개월</option>
      </select>
    </div>

    <div class="row mt-4">
      <div v-if="selectedOptions.includes('deposit')" class="col-6">
        <h3>예금</h3>
        <DepositList :korCoName="selectedKorCoName" :saveTerm="parseInt(selectedSaveTerm)"/>
      </div>
      <div v-if="selectedOptions.includes('saving')" class="col-md-6">
        <h3>적금</h3>
        <SavingList :korCoName="selectedKorCoName" :saveTerm="parseInt(selectedSaveTerm)"/>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useProductStore } from '@/stores/product'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'

const store = useProductStore()
const selectedOptions = ref([])
const selectedKorCoName = ref('')
const selectedSaveTerm = ref(0)


const korCoNames = computed(() => store.korCoNames)
const saveTrm = computed(() => store.saveTrm)




</script>

<style scoped>
.container {
  background-color: #f7feff;
  padding: 30px;



}
.outer-container {
  padding: 20px;
  /* margin-bottom: 20px; */
}


.form-check {
  margin-right: 20px;
}

.form-select {
  width: 200px;
  margin-top: 10px;
}


</style>
