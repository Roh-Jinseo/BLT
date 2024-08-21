<template>
  <nav class="nav">
    <RouterLink class="link" :to="{ name: 'ProfileView', params: { username: username } }">프로필</RouterLink>
    <RouterLink class="link" :to="{ name: 'ProfileProductView', params: { username: username } }">가입한 상품 목록</RouterLink>
    <RouterLink class="link" :to="{ name: 'ProfileUpdateView', params: { username: username } }">프로필 수정</RouterLink>
  </nav>
  
  <div class="container">
    <h1>가입한 상품 목록</h1>
    <div v-for="(product, index) in subscribedProducts" :key="index" class="product">
      <div v-if="getProductDetails(product)">
        <h2>{{ getProductDetails(product).kor_co_nm }} - {{ getProductDetails(product).fin_prdt_nm }}</h2>
        <button @click="navigateToDetail(product)" class="btn btn-outline-dark">상세 보기</button>
        <hr>
        <p>{{ getProductDetails(product).etc_note }}</p>
        <!-- <ul>
          <li v-for="option in getProductDetails(product).options" :key="option.id">
            {{ option.intr_rate_type_nm }} - {{ option.save_trm }}개월 - {{ option.intr_rate }}%
          </li>
        </ul> -->
      </div>
      <div v-else>
        <p>상품 정보를 찾을 수 없습니다: {{ product }}</p>
      </div>
      <br>
    </div>
    <BarChart :chartData="chartData" :chartOptions="chartOptions" />
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { useProductStore } from '@/stores/product'
import BarChart from '@/components/BarChart.vue'

const router = useRouter()
const userStore = useCounterStore()
const productStore = useProductStore()
const subscribedProducts = userStore.userInfo.financial_products.split(',')
const username = userStore.saveUsername


// 상품 ID를 기반으로 productStore에서 상품 정보를 가져오는 함수
const getProductDetails = (productId) => {
  const depositProduct = productStore.depositOptionCombine.find(product => product.fin_prdt_cd === productId)
  const savingProduct = productStore.savingOptionCombine.find(product => product.fin_prdt_cd === productId)
  return depositProduct || savingProduct
}

const navigateToDetail = (productId) => {
  const productDetails = getProductDetails(productId)
  if (productDetails) {
    const routeName = productStore.depositOptionCombine.some(product => product.fin_prdt_cd === productId)
      ? 'ProductDepositDetailView'
      : 'ProductSavingDetailView'
    router.push({ name: routeName, params: { fin: productDetails.fin_prdt_cd } })
  }
}

// 각 상품의 이름, 기본 금리, 최고 우대 금리를 저장할 배열
const productsData = ref([])

subscribedProducts.forEach(productId => {
  const productDetails = getProductDetails(productId)
  if (productDetails) {
    const option = productDetails.options[0]
    if (option) {
      productsData.value.push({
        name: productDetails.fin_prdt_nm,
        baseRate: option.intr_rate,
        preferredRate: option.intr_rate2
      })
    }
  }
})

// Chart.js 데이터와 옵션 설정
const chartData = ref({
  labels: ['평균', ...productsData.value.map(product => product.name)],
  baseRates: [average(productsData.value.map(product => product.baseRate)), ...productsData.value.map(product => product.baseRate)],
  preferredRates: [average(productsData.value.map(product => product.preferredRate)), ...productsData.value.map(product => product.preferredRate)]
})

const chartOptions = ref({
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    data: ['기본 금리', '최고 우대 금리']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: chartData.value.labels
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      formatter: '{value}%'
    }
  }
})

// 평균 계산 함수
function average(arr) {
  const sum = arr.reduce((a, b) => a + b, 0)
  return (sum / arr.length).toFixed(2)
}
</script>

<style scoped>
.product {
  background-color: #f9f9f9;

}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}

h2 {
  font-size: 1.5em;
  margin: 10px 0;
}

p {
  margin: 5px 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #f9f9f9;
  margin: 5px 0;
  padding: 10px;
  border-radius: 5px;
}

div {
  margin-bottom: 20px;
}

.nav   {
  margin-right: 10px;
  text-decoration: none;
  /* color: black; */
  color: skyblue;
  font: small-caps bold 18px/1 sans-serif;
}
.link {
  text-decoration: none;
  color: black;
  margin: 10px;
}

.container{
  /* margin: 0 auto; */
  padding: 20px;
  /* max-width: 800px; */
}
</style>
