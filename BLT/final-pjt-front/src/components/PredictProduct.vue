<template>
  <div>
    <h2>상품 추천</h2>
    <hr>
    <div v-if="!userStore.isLogin">
      <p>로그인 하시면 상품 추천 결과를 확인하실 수 있습니다.</p>
      <div v-if="topProducts.length">
        <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" v-for="(product, index) in topProducts" :key="index" :data-bs-target="'#carouselExampleCaptions'" :data-bs-slide-to="index" :class="{'active': index === 0}" :aria-label="'Slide ' + (index + 1)"></button>
          </div>
          <div class="carousel-inner">
            <div v-for="(product, index) in topProducts" :key="index" :class="['carousel-item', { active: index === 0 }]">
              <img src="@/assets/배경사진.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>{{ product.fin_prdt_nm }}</h5>
                <p>{{ product.kor_co_nm }}</p>
                <p>{{ product.etc_note }}</p>
                <button class="btn btn-outline-dark" @click="showProductDetails(product)">상세 정보 보기</button>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <div v-if="!userInfo">
        <p>사용자 정보를 불러오는 중입니다...</p>
      </div>
      <div v-else>
        <h4>{{ userInfo.last_name }}{{ userInfo.first_name }}님께 어울리는 상품이에요!</h4>
        <div v-if="predictions.length">
          <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
              <button type="button" v-for="(prediction, index) in predictions" :key="index" :data-bs-target="'#carouselExampleCaptions'" :data-bs-slide-to="index" :class="{'active': index === 0}" :aria-label="'Slide ' + (index + 1)"></button>
            </div>
            <div class="carousel-inner">
              <div v-for="(prediction, index) in predictions" :key="index" :class="['carousel-item', { active: index === 0 }]">
                <img src="@/assets/배경사진.jpg" class="d-block w-100" alt="...">
                <div class="carousel-caption">
                  <h5>{{ getProductDetails(prediction.product).fin_prdt_nm }}</h5>
                  <p>{{ getProductDetails(prediction.product).kor_co_nm }}</p>
                  <p>{{ getProductDetails(prediction.product).etc_note }}</p>
                  <button class="btn btn-outline-light" @click="showProductDetails(getProductDetails(prediction.product))">상세 정보 보기</button>
                </div>
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
        <div v-else>
          <p>예측 결과를 불러오는 중입니다...</p>
        </div>
      </div>
    </div>

    <!-- Product Details Modal -->
    <div class="modal fade" id="productDetailsModal" tabindex="-1" aria-labelledby="productDetailsModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="productDetailsModalLabel">{{ selectedProduct.fin_prdt_nm }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>은행명:</strong> {{ selectedProduct.kor_co_nm }}</p>
            <p><strong>상품코드:</strong> {{ selectedProduct.fin_prdt_cd }}</p>
            <p><strong>가입방법:</strong> {{ selectedProduct.join_way }}</p>
            <p><strong>가입대상:</strong> {{ selectedProduct.join_member }}</p>
            <p><strong>기타사항:</strong> {{ selectedProduct.etc_note }}</p>
            <p><strong>금리 정보:</strong></p>
            <ul>
              <li v-for="option in selectedProduct.options" :key="option.id">
                {{ option.intr_rate_type_nm }} - {{ option.intr_rate }}% (우대: {{ option.intr_rate2 }}%)
              </li>
            </ul>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watchEffect } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useProductStore } from '@/stores/product'

const userStore = useCounterStore()
const productStore = useProductStore()
const predictions = ref([])
const topProducts = ref([]) // 로그인하지 않았을 때 보여줄 상품
const userInfo = computed(() => userStore.userInfo)
const selectedProduct = ref({})

const getPredictions = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/financial/predict/', {
      age: userInfo.value?.age || 0,
      currentAsset: userInfo.value?.currentAsset || 0,
      salary: userInfo.value?.salary || 0,
      gender: userInfo.value?.gender || 0
    })
    predictions.value = response.data.predictions
  } catch (error) {
    console.error('Error fetching predictions:', error)
  }
}

const getTopProducts = () => {
  // depositOptionCombine에서 최고 우대 금리가 높은 2개의 상품
  const topDeposits = productStore.depositOptionCombine
    .sort((a, b) => b.options[0].intr_rate2 - a.options[0].intr_rate2)
    .slice(0, 2)

  // savingOptionCombine에서 최고 우대 금리가 높은 2개의 상품
  const topSavings = productStore.savingOptionCombine
    .sort((a, b) => b.options[0].intr_rate2 - a.options[0].intr_rate2)
    .slice(0, 2)

  topProducts.value = [...topDeposits, ...topSavings]
}

const getProductDetails = (fin_prdt_cd) => {
  return productStore.depositOptionCombine.find(product => product.fin_prdt_cd === fin_prdt_cd) ||
    productStore.savingOptionCombine.find(product => product.fin_prdt_cd === fin_prdt_cd) || {}
}

const showProductDetails = (product) => {
  selectedProduct.value = product
  const modal = new bootstrap.Modal(document.getElementById('productDetailsModal'))
  modal.show()
}

onMounted(async () => {
  await productStore.getDepositOptionCombine()
  await productStore.getSavingOptionCombine()

  if (userStore.isLogin && userInfo.value) {
    await getPredictions()
  } else {
    getTopProducts()
  }
})

// watch를 사용하여 로그인 상태가 변경될 때마다 상품 목록을 업데이트
watchEffect(async () => {
  if (userStore.isLogin && userInfo.value) {
    await getPredictions()
  } else {
    getTopProducts()
  }
})
</script>

<style scoped>
/* 기본 크기 */
.carousel-caption h5 {
  font-size: calc(3.0vw);
}

.carousel-caption p {
  font-size: calc(1.2vw);
}

.carousel-caption button {
  font-size: calc(1.5vw);
}
</style>
