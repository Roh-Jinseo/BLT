
<template>
  <div style="background-color:#B2DFDB">
  <div class="container mt-4">
    <h1 class="small-caps sans-serif" style="color:black;">은행 지점 검색</h1>
    <form @submit.prevent="onsubmit">
      <div>
        <!-- <div  style="padding-right: 0;"> -->
          <label for="select1" >시/도 선택:</label>
          <select id="select1" v-model="selectedCity" @change="updateDistricts"  style="margin-right:10px; color: black; border-color: #B2DFDB;">
            <option value="" disabled>시/도를 선택하세요</option>
            <option v-for="(districts, city) in regions" :key="city" :value="city">{{ city }}</option>
          </select>
        <!-- </div> -->
        <!-- <div > -->
          <label for="select2">구/군 선택:</label>
          <select id="select2" v-model="selectedDistrict" style="margin-right:10px; color: black; border-color: #B2DFDB;">
            <option value="" disabled>구/군을 선택하세요</option>
            <option v-for="district in districts" :key="district">{{ district }}</option>
          </select>
        <!-- </div> -->
        <!-- <div > -->
          <label for="select3">은행 선택:</label>
          <select id="select3" v-model="selectedBank" style="margin-right:10px; color: black; border-color: #B2DFDB;">
            <option value="" disabled>은행을 선택하세요</option>
            <option v-for="bank in banks" :key="bank">{{ bank }}</option>
          </select>
        <!-- </div> -->

        <!-- <p>{{ selectedCity }} {{ selectedDistrict }} {{ selectedBank }}</p> -->

        <KakaoMap 
      :keyword="keyword"
        />
      </div>
      </form>

  </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue'
import KakaoMap from '@/components/KakaoMap.vue'

export default {
  components: { KakaoMap },
  
  setup() {
    const selectedCity = ref('')
    const selectedDistrict = ref('')
    const selectedBank = ref('')
    const keyword = ref('')

    const regions = ref({
      "서울특별시": ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"],
      "부산광역시": ["중구", "서구", "동구", "영도구", "부산진구", "동래구", "남구", "북구", "해운대구", "사하구", "금정구", "강서구", "연제구", "수영구", "사상구", "기장군"],
      "대구광역시": ["중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군", "군위군"],
      "인천광역시": ["중구", "동구", "미추홀구", "연수구", "남동구", "부평구", "계양구", "서구", "강화군", "옹진군"],
      "광주광역시": ["동구", "서구", "남구", "북구", "광산구"],
      "대전광역시": ["동구", "중구", "서구", "유성구", "대덕구"],
      "울산광역시": ["중구", "남구", "동구", "북구", "울주군"],
      "세종특별자치시": ["세종특별자치시"],
      "경기도": ["수원시", "용인시", "고양시", "화성시", "성남시", "부천시", "남양주시", "안산시", "평택시", "안양시", "시흥시", "파주시", "김포시", "의정부시", "광주시", "하남시", "광명시", "군포시", "양주시", "오산시", "이천시", "안성시", "구리시", "의왕시", "포천시", "양평군", "여주시", "동두천시", "과천시", "가평군", "연천군"],
      "강원특별자치도": ["춘천시", "원주시", "강릉시", "동해시", "태백시", "속초시", "삼척시", "홍천군", "횡성군", "영월군", "평창군", "정선군", "철원군", "화천군", "양구군", "인제군", "고성군", "양양군"],
      "충청북도": ["청주시", "충주시", "제천시", "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군", "음성군", "단양군"],
      "충청남도": ["천안시", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군"],
      "전북특별자치도": ["전주시", "군산시", "익산시", "정읍시", "남원시", "김제시", "완주군", "진안군", "무주군", "장수군", "임실군", "순창군", "고창군", "부안군"],
      "전라남도": ["목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", "고흥군", "보성군", "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", "함평군", "영광군", "장성군", "완도군", "진도군", "신안군"],
      "경상북도": ["포항시", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", "상주시", "문경시", "경산시", "의성군", "청송군", "영양군", "영덕군", "청도군", "고령군", "성주군", "칠곡군", "예천군", "봉화군", "울진군", "울릉군"],
      "경상남도": ["창원시", "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군", "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군"],
      "제주특별자치도": ["제주시", "서귀포시"]
    })

    const districts = ref([])
    const banks = [
      'KEB하나은행', 'SC제일은행', '국민은행',
      '신한은행', '외환은행', '우리은행',
      '한국시티은행', '지방은행',
      '경남은행', '광주은행', '대구은행',
      '부산은행', '전북은행', '제주은행',
      '특수은행', '기업은행', '농협은행', '수협은행',
      '한국산업은행', '한국수출입은행'
    ]

    const updateDistricts = () => {
      districts.value = regions.value[selectedCity.value] || []
      selectedDistrict.value = ''
      selectedBank.value = ''
    }
    const onsubmit = function(){
      keyword.value = `${ selectedCity } ${ selectedDistrict } ${ selectedBank }`
    }
    watch([selectedCity, selectedDistrict, selectedBank], ([newCity, newDistrict, newBank]) => {
      keyword.value = `${newCity} ${newDistrict} ${newBank}`
    })

    return {
      selectedCity,
      selectedDistrict,
      selectedBank,
      keyword,
      regions,
      districts,
      banks,
      updateDistricts
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 20px;
  
}

.profile-container {
  /* background-color: #B2DFDB; */
  /* background-color: #1565C0 #03A9F4 skyblue #80D8FF; */
  display: flex;
  flex-direction: column;
  align-items: center;
  /* padding-left: 120px; */
  /* border-radius: 10px; */
  height: 50rem;
  text-align: left;
}


#map {
  width: 100%;
  height: 500px;
}
#menu_wrap {
  position: absolute;
  top: 0;
  left: 0;
  width: 250px;
  height: 500px;
  overflow-y: auto;
  background: rgba(255, 255, 255, 0.9);
}
.item {
  cursor: pointer;
  padding: 10px;
}
.item:hover {
  background: #f1f1f1;
}
#pagination {
  margin: 10px 0;
  text-align: center;
}
#pagination a {
  display: inline-block;
  margin-right: 5px;
  text-decoration: none;
}
#pagination .on {
  font-weight: bold;
  color: red;
}
</style>