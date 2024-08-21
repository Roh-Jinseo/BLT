<template>
  <div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const store = useCounterStore()
const router = useRouter()
onMounted(()=>{
  store.logout()
  router.push({name:'MainView'})
})
</script>

<style scoped>

</style>