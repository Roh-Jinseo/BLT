<template>
  <div v-if="depositInfo" class="container mt-4">
    <!-- 로그인 상태인 경우에만 버튼 생성 -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="mb-0">{{ depositInfo.fin_prdt_nm }} 상세정보</h2>
        <div v-if="userStore.token">
          <button @click="joinRemoveProduct(depositInfo.fin_prdt_cd)" class="btn btn-primary">
            {{ isSubscribed ? '가입 취소' : '가입하기' }}
          </button>
        </div>
    </div>
    <div class="card mb-4">
      <div class="card-body">
        <p class="card-text"><strong>은행:</strong> {{ depositInfo.kor_co_nm }}</p>
        <p class="card-text"><strong>가입방법:</strong> {{ depositInfo.join_way }}</p>
        <p class="card-text"><strong>특이사항:</strong> {{ depositInfo.etc_note }}</p>
        <p class="card-text"><strong>가입제한:</strong> {{ depositInfo.join_deny }}</p>
        <p class="card-text"><strong>가입대상:</strong> {{ depositInfo.join_member }}</p>
        <p class="card-text"><strong>특별조건:</strong> {{ depositInfo.spcl_cnd }}</p>
      </div>
    </div>

    <h3>옵션 정보</h3>
    <div class="row">
      <div v-for="option in depositInfo.options" :key="option.id" class="col-md-4 mb-4">
        <div class="card h-100">
          <div class="card-body">
            <p class="card-text"><strong>저장 기간:</strong> {{ option.save_trm }}개월</p>
            <p class="card-text"><strong>금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
            <p class="card-text"><strong>이율:</strong> {{ option.intr_rate }}%</p>
            <p class="card-text"><strong>복리 이율:</strong> {{ option.intr_rate2 }}%</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-else>
    <p>로딩 중 입니다.</p>
  </div>
</template>

<script setup>
import { onMounted, ref,computed } from 'vue'
import { useProductStore } from '@/stores/product'
import { useCounterStore } from '@/stores/counter'
import { useRoute,useRouter } from 'vue-router'
import axios from 'axios'

const store = useProductStore()
const route = useRoute()
const router = useRouter()
const userStore = useCounterStore()
const depositInfo = computed(() => {
  return store.depositOptionCombine.find(deposit => deposit.fin_prdt_cd === route.params.fin);
})


const isSubscribed =ref(false)


const joinRemoveProduct = function(fin_prdt_cd) {

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/financial/join-product/${fin_prdt_cd}`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
  .then(response => {
    alert(response.data.message)
    // 가입 취소 메시지인 경우
    if (response.data.message === '가입 취소!') {
      // 가입 상태를 false로 업데이트
      isSubscribed.value = false
      // 유저정보 업데이트
      userStore.getUserInfo()
      // router.push({name:'ProfileProductview',params:{username:userStore.saveUsername}})
    } else {
      // 가입 상태를 true로 업데이트
      isSubscribed.value = true
      // 유저정보 업데이트
      userStore.getUserInfo()
      // router.push({name:'ProfileProductview',params:{username:userStore.saveUsername}})

    }
  })
  .catch(error => {
    if (error.response && error.response.data && error.response.data.error) {
      alert(error.response.data.error)
    } else {
      console.log(error)
    }
  })
}

onMounted(() => {
  store.getDepositOption(route.params.fin);
  if (userStore.userInfo){
  isSubscribed.value=userStore.userInfo.financial_products.split(',').includes(depositInfo.value.fin_prdt_cd)
  }
})
</script>

<style scoped>
.card {
  margin-bottom: 1rem;
}
.card-title {
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
}
.card-text {
  margin-bottom: 0.5rem;
}
</style>
