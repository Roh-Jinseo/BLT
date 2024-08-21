import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useCounterStore } from './counter'

export const useProductStore = defineStore('product', () => {
    const API_URL = 'http://127.0.0.1:8000'
    const depositOption =ref([])
    const depositOptionCombine = ref([])
    const savingOption =ref([])
    const savingOptionCombine = ref([])
    const korCoNames = ref([])
    const saveTrm = ref([])


    // 여기는 예금 


    const getDepositOption = function (fin_cd) {
        axios({
            method: 'get',
            url: `${API_URL}/financial/deposit-product-options/${fin_cd}/`,
        })
            .then(response => {
            depositOption.value = response.data
            updateSaveTrm()
            })
            .catch(error => {
            console.log(error)
            })
        }



    const getDepositOptionCombine = function() {
            axios({
            method: 'get',
            url: `${API_URL}/financial/combined-deposit-products/`,
            })
            .then(response => {
                depositOptionCombine.value = response.data
                updateKorCoNames()
                updateSaveTrm
            })
            .catch(error => {
                console.log(error)
            })
        }



    // 여기부터는 적금 


    const getSavingOption = function (fin_cd) {
        axios({
            method: 'get',
            url: `${API_URL}/financial/saving-product-options/${fin_cd}/`,
        })
            .then(response => {
            savingOption.value = response.data
            updateSaveTrm()
            })
            .catch(error => {
            console.log(error)
            })
        }

    const getSavingOptionCombine = function() {
        axios({
            method: 'get',
            url: `${API_URL}/financial/combined-saving-products/`,
        })
            .then(response => {
            savingOptionCombine.value = response.data
            updateKorCoNames()
            updateSaveTrm()
            })
            .catch(error => {
            console.log(error)
            })
    }

    const updateKorCoNames = function () {
        const allKorCoNames = [...depositOptionCombine.value, ...savingOptionCombine.value].map(item => item.kor_co_nm)
        korCoNames.value = [...new Set(allKorCoNames)]
      }
    
    
    
    
    
    const updateSaveTrm = function() {
        // 각 상품 옵션의 save_trm 값을 추출하여 하나의 배열로 합치기
        const depositTerms = depositOptionCombine.value.flatMap(option => option.options.map(opt => opt.save_trm))
        const savingTerms = savingOptionCombine.value.flatMap(option => option.options.map(opt => opt.save_trm))
      
        // 중복된 값을 제거하고 정렬
        const allTerms = [...new Set([...depositTerms, ...savingTerms])].sort((a, b) => a - b)
        
        // saveTrm 업데이트
        saveTrm.value = allTerms
      }


    

  return {
    depositOption,getDepositOption,depositOptionCombine,getDepositOptionCombine,
    savingOption,getSavingOption,savingOptionCombine,getSavingOptionCombine,
    korCoNames,saveTrm
    }
}, { persist: true })
