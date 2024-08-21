<template>
  <!-- <div style="background-color: ;"> -->
    <!-- <nav class="nav"></nav> -->
  <main class="container mt-5">
    <h1 class="text-center mb-4">환율 계산기</h1>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow-sm">
          <div class="card-body">
            <div class="mb-3">
              <label for="fromCurrency" class="form-label">환전 국가</label>
              <select id="fromCurrency" v-model="selectedCurrency" class="form-select">
                <option value="" disabled>국가를 선택하세요</option>
                <option v-for="rate in exchangeRates" :key="rate.id" :value="rate">{{ rate.cur_nm }}</option>
              </select>
            </div>
            <div class="mb-3">
              <label for="fromAmount" class="form-label">금액을 입력하세요 ({{ selectedCurrency ? selectedCurrency.cur_unit : '' }})</label>
              <input type="text" @input="(event) => changeasd(event,0)" :value="toAmount" id="fromAmount" class="form-control" placeholder="금액">
            </div>
            <div class="mb-3">
              <p class="mb-4">금액을 입력하세요 (KRW)</p>
              <input type="text" @input="(event) => changeasd(event,1) " :value="fromAmount" id="toAmount" class="form-control" placeholder="금액">
            </div>
          </div>
        </div>
      </div>
    </div>
    
  </main>
<!-- </div> -->
</template>

<script setup>
import { ref, computed, watchEffect  } from 'vue';
import axios from 'axios';
import { useExchangerStore } from '@/stores/exchanger';

const exchangeRates = ref([]);
const selectedCurrency = ref(null);
const toAmount = ref(null);
const fromAmount = ref(null);
const store = useExchangerStore();

// 환율 정보 가져오기
axios({
  method: 'get',
  url: 'http://localhost:8000/exchange/save-exchange-rates/',
}).then(res => {
  exchangeRates.value = res.data.response;
}).catch(error => {
  console.error(error);
});


// 아래 입력창의 국가는 한국으로 고정
const toCurrency = computed(() => exchangeRates.value.find(rate => rate.cur_nm === '한국') || null);

// 위 입력창에서 금액이 변경될 때마다 실시간으로 계산하여 아래 입력창에 반영
// watchEffect(() => {
  // if (!selectedCurrency.value || !fromAmount.value) return;
  // const exchangeRate = parseFloat(selectedCurrency.value.deal_bas_r.replace(/,/g, ''));
  // const amountKRW = parseFloat(fromAmount.value) * exchangeRate;
  // toAmount.value = parseInt(amountKRW);
// });
// watchEffect(() => {
//   if (!selectedCurrency.value || !fromAmount.value) return;
//   const exchangeRate = parseFloat(selectedCurrency.value.deal_bas_r.replace(/,/g, ''));
//   const amountKRW = parseFloat(toAmount.value) * exchangeRate;
//   fromAmount.value = parseInt(amountKRW);
// });

const changeasd = (event, who) => {
  if (!selectedCurrency.value) {
    alert('국가를 선택해주세요.'); // 국가가 선택되지 않은 경우 경고 메시지 표시
    return;
  }

  if (who === 0) {
    toAmount.value = parseInt(event.target.value)
    const exchangeRate = parseFloat(selectedCurrency.value.deal_bas_r.replace(/,/g, ''));
    const amountKRW = parseFloat(event.target.value) * exchangeRate;
    fromAmount.value = parseInt(amountKRW)
  } else if (who === 1) {
    fromAmount.value = parseInt(event.target.value)
    const exchangeRate = parseFloat(selectedCurrency.value.deal_bas_r.replace(/,/g, ''));
    const amountKRW = parseFloat(event.target.value) / exchangeRate;
    toAmount.value = parseInt(amountKRW)
  }
}


</script>

<style scoped>
main {
  font-family: 'WooridaumB';
}
.card {
  border: none;
  border-radius: 10px;
}




</style>
