<template>
  <div>
    <DepositListItem 
      v-for="deposit in filteredDeposits"
      :key="deposit.fin_prdt_cd"
      :deposit="deposit"
      class="card mb-4"

    />
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
import { computed } from 'vue'
import DepositListItem from '@/components/DepositListItem.vue'

const store = useProductStore()
const props = defineProps({
  korCoName: String,
  saveTerm: Number
})

const filteredDeposits = computed(() => {
  return store.depositOptionCombine.filter(deposit => {
    // 필터 조건: 회사 이름과 저장 기간이 일치하는지 확인
    const matchKorCoName = props.korCoName ? deposit.kor_co_nm === props.korCoName : true;
    const matchSaveTerm = props.saveTerm ? deposit.options.some(option => option.save_trm === props.saveTerm) : true;

    return matchKorCoName && matchSaveTerm;
  })
})
</script>

<style scoped>
</style>
