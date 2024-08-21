import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangerStore = defineStore('exchanger', () => {
  const rates = ref([])
  const BASE_URL = 'http://localhost:8000'

  const getRates = function() {
    axios({
      method: 'get',
      url: `${BASE_URL}/exchange/exchange-rates/`
    })
      .then(res => {
        // console.log(res.data)
        rates.value = res.data

      })
      .catch(err => console.log(err))
  }

  return {rates, BASE_URL, getRates }
}, { persist: true })
