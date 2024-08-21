<template>
  <div class="exchange-main card shadow">
    <h3 class="text-center card-header">환율 정보</h3>
    <div class="card-body">
      <div v-for="currency in currencies" :key="currency.id" class="currency-row">
        <div class="flag-icon">
          <img :src="getFlagImagePath(currency.cur_nm)" alt="flag">
        </div>
        <div class="currency-info">
          <h6 class="card-title">{{ currency.cur_nm }}</h6>
          <p class="card-text">{{ currency.deal_bas_r }} 원</p>
        </div>
      </div>
    </div>
  
  </div>

    <div class="exchange-main card shadow">
      <h4 class="text-center card-header">알쓸 금융</h4>
      <div class="card-body">
        <a href="https://www.fss.or.kr/edu/main/contents.do?menuNo=300041" style="text-decoration: none; color: black;">나의 금융지식 수준은?</a> <br>
        <a href="https://fine.fss.or.kr/fine/fnctip/dpstCalc/view.do?menuNo=900018" style="text-decoration: none; color: black;">예적금 계산기</a> <br>
        <a href="https://www.bok.or.kr/portal/bbs/B0000216/view.do?type=YNGBGS&nttId=10075809&menuNo=200647" style="text-decoration: none; color: black;">경제금융용어 700선</a>
      </div>
    </div>


    

</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const currencies = ref([])

onMounted(() => {
  axios.get('http://localhost:8000/exchange/save-exchange-rates/')
    .then(res => {
      currencies.value = res.data.response.filter(currency => {
        // 필요한 환율 정보만 필터링
        return ['위안화', '유로', '일본 옌', '미국 달러'].includes(currency.cur_nm)
      })
    })
    .catch(error => {
      console.error(error)
    })
})

const getFlagImagePath = (currencyName) => {
  // 각 국가에 따른 국기 이미지 경로 반환 (실제 경로는 적절하게 수정해주세요)
  // 예: return `/images/flags/${currencyName}.png`
  return `https://flagcdn.com/48x36/${getCountryCode(currencyName)}.png`
}

const getCountryCode = (currencyName) => {
  // 각 국가에 따른 ISO 3166-1 alpha-2 코드 반환 (실제 코드는 적절하게 수정해주세요)
  switch (currencyName) {
    case '위안화':
      return 'cn'
    case '유로':
      return 'eu'
    case '일본 옌':
      return 'jp'
    case '미국 달러':
      return 'us'
    default:
      return ''
  }
}
</script>

<style scoped>
.exchange-main {
  text-align: center;
  padding: 20px;
  margin-bottom: 20px;
}

.currency-row {
  display: flex;
  align-items: center;
  margin-bottom: 10px; /* 각 환율 정보 간격 */
}

.flag-icon {
  margin-right: 20px;
}

.flag-icon img {
  width: 50px; /* 국기 이미지 크기 조정 */
  height: auto;
}


</style>
