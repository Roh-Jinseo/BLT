<template>
  <div>
    <p>exchangeRates List </p>
    <!-- <form @submit.prevent="createArticle"> -->
      <!-- <p>환전할 국가를 선택하시오.</p> -->
      <select id="country" v-model="selected">
        <option v-for="rate in rates" :rate="rate" :key="rate.id" :value="rate">
          {{ rate.cur_nm }}
        </option>
      </select>

        <!-- <label for="inputMoney">환전할금액 : </label> -->
        <input type="text" v-model.trim="inputMoney" id="inputMoney" placeholder="금액을 입력하세요">
        <!-- <input type="submit" value="rate.cur_unit"> -->
        <button  @click="calcToWon">통화 {{selected.cur_unit}}</button>
      <div>
          <label for="outputMoney"> : </label>
          <input type="text" v-model.trim="outputMoney" id="outputMoney">
          <button @click="calcToMoney"> ₩ </button>
      </div>
      <!-- <p>선택출력: {{selected}}</p> -->
      <!-- deal_bas_r -->

  </div>
</template>

<script setup>
import {ref} from 'vue'

const selected = ref('')
const unit = ref(null)
const inputMoney = ref('0')
const outputMoney = ref('0')

defineProps({
  rates: Array,
});

const calcToWon = function () {
  console.log("clicked")
  outputMoney.value = parseFloat(inputMoney.value)*parseFloat(selected.value.deal_bas_r)
  // console.log(rate)
}
const calcToMoney = function () {
  console.log("clicked")
  inputMoney.value = parseFloat(outputMoney.value)/parseFloat(selected.value.deal_bas_r)
  // console.log(rate)
}
</script>

<style scoped>

</style>