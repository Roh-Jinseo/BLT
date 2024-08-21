import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogOutView from '@/views/LogOutView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileProductView from '@/views/ProfileProductView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'


// 환율계산기
import ExchangeRatesView from '@/views/ExchangeRatesView.vue'
// 금융상품
import ProductView from '@/views/ProductView.vue'
import ProductDepositDetailView from '@/views/ProductDepositDetailView.vue'
import ProductSavingDetailView from '@/views/ProductSavingDetailView.vue'
// 지도
import MapView from '@/views/MapView.vue'
//
import AboutUsView from '@/views/AboutUsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'MainView',
      component:MainView,
    },
    {
      path: '/article',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/article_create',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },
    {
      path: '/article_edit/:id',
      name: 'ArticleEditView',
      component: ArticleEditView
    },
    // user
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'LogOutView',
      component: LogOutView
    },

    {
      path: '/profile/:username',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/profile_update/:username',
      name: 'ProfileUpdateView',
      component: ProfileUpdateView
    },
    {
      path: '/profile-product/:username',
      name: 'ProfileProductView',
      component: ProfileProductView
    },
    // 금융상품
    {
      path: '/product',
      name: 'ProductView',
      component: ProductView,
    },  
    {
      path: '/product/deposit/:fin',
      name: 'ProductDepositDetailView',
      component: ProductDepositDetailView
    },
    {
      path: '/product/saving/:fin',
      name: 'ProductSavingDetailView',
      component: ProductSavingDetailView
    },
    // 환율계산기
    {
      path: '/exchangeRates',
      name: 'ExchangeRatesView',
      component: ExchangeRatesView
    },
    // 지도
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    // about us
    {
      path: '/about',
      name: 'AboutUsView',
      component: AboutUsView
    },
  ]
})

import { useCounterStore } from '@/stores/counter'


router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'MainView' }
  }
})

export default router
