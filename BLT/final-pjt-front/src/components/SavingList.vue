<template>
    <div>
      <SavingListItem 
        v-for="saving in filteredSavings"
        :key="saving.fin_prdt_cd"
        :saving="saving"
        class="card mb-4"
      />
    </div>
  </template>
  
  <script setup>
  import { useProductStore } from '@/stores/product';
  import { computed } from 'vue'
  import SavingListItem from '@/components/SavingListItem.vue'
  
  const store = useProductStore()
  const props = defineProps({
    korCoName: String,
    saveTerm: Number
  })
  
  const filteredSavings = computed(() => {
    return store.savingOptionCombine.filter(saving => {
      // 필터 조건: 회사 이름과 저장 기간이 일치하는지 확인
      const matchKorCoName = props.korCoName ? saving.kor_co_nm === props.korCoName : true;
      const matchSaveTerm = props.saveTerm ? saving.options.some(option => option.save_trm === props.saveTerm) : true;
  
      return matchKorCoName && matchSaveTerm;
    })
  })
  </script>
  
  <style scoped>
  </style>
  