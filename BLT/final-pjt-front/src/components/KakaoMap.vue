<template>
  <div class="container">
    <div class="map-container">
      <div class="search-bar">
        <button @click="onLoadKakaoMap" type="submit" class="btn btn-outline-dark" style="margin-right: 1rem;">검색</button> 
        <!-- <button @click="onLoadKakaoMap" type="submit" style="color: black; border-color: #B2DFDB;">검색</button>  -->
      </div>

    
      <KakaoMap :lat="lat" :lng="lng" @onLoadKakaoMap="onLoadKakaoMap" style="margin-right:10px; color: black; border-color: #B2DFDB;">
        <KakaoMapMarker
          v-for="(marker, index) in markerList"
          :key="marker.key === undefined ? index : marker.key"
          :lat="marker.lat"
          :lng="marker.lng"
          :infoWindow="marker.infoWindow"
          :clickable="true"
          @onClickKakaoMapMarker="onClickMapMarker(marker)"
        />
      </KakaoMap>
    </div>
    <div class="marker-list">
      <div v-for="marker in markerList" :key="marker.infoWindow.placeName" class="marker-item">
        <p>지점명: {{ marker.infoWindow.placeName }}</p>
        <p>지점주소: {{ marker.infoWindow.address }}</p>
        <p>도로명주소: {{ marker.infoWindow.road_address }}</p>
        <p>연락처: {{ marker.infoWindow.phone }}</p>
        <a :href="marker.infoWindow.place_url" target="_blank"><p>URL</p></a>
        <hr>
      </div>
    </div>
  </div>
</template>


<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
import {ref, defineProps} from 'vue'


// selectedCity :String,
// selectedDistrict :String,
// selectedBank :String,
const props = defineProps({
  keyword: String
})


//검색 저장
const searchWord = ref('')
//라이브러리 사용 방법을 반드시 참고하여 주시기 바랍니다.
const map = ref();
const markerList = ref([]);
const lat = ref(33.450701);
const lng = ref(126.570667);
const testy = ref('')

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  markerList.value = [] // marker리스트 초기화
  // console.log(markerList.value)
  // searchWord.value = `${selectedCity}`
  console.log(searchWord.value)
  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places();
  // 키워드로 장소를 검색합니다
  // ps.keywordSearch('역삼역 맛집', placesSearchCB);
  console.log(props.keyword)
  searchWord.value = props.keyword
  console.log(searchWord.value)
  ps.keywordSearch(searchWord.value, placesSearchCB);
};

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    const bounds = new kakao.maps.LatLngBounds();
    let latAvg = 0
    let lngAvg = 0
    console.log("data", data)
    for (let marker of data) {
      const markerItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          placeName: marker.place_name,
          address: marker.address_name,
          road_address: marker.road_address_name,
          phone : marker.phone,
          place_url : marker.place_url,
          visible: false
        }
      };
      // console.log("각각의 경도위도 출력", parseFloat(marker.y))
      latAvg += parseFloat(marker.y)
      lngAvg += parseFloat(marker.x)

      markerList.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    console.log("print",map.value)
    console.log("bounds",bounds)
    // console.log(lat, lng)
    if(markerList.value){
      lat.value = markerList.value[0].lat
      lng.value = markerList.value[0].lng
      
      // lat.value = latAvg / markerList.value.length
      // lng.value = lngAvg / markerList.value.length
      console.log("avg",latAvg, lngAvg)

      console.log(markerList.value[0].lat, markerList.value[0].lng)
    }else{
      window.alert("검색결과가 없습니다.")
    }
    map.value?.setBounds(bounds);
  }
};

//마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다
const onClickMapMarker = (markerItem) => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};
</script>
<style scoped>
.container {
  display: flex;
  /* flex-direction: column; */
  width: 100%;
  margin-top: 20px;
  
  /* background-color: whitesmoke; */
}

.map-container {
  flex: 1;
  position: relative;
  height: 80vh;
}

.marker-list {
  flex: 1;
  max-height: 60vh; /* Set a maximum height for the marker list */
  overflow-y: auto; /* Enable vertical scrolling */
  padding-left: 20px;
  border: 1px solid #B2DFDB;;
  /* border-radius: 20px; */
  background-color:  whitesmoke;
}

.search-bar {
  text-align: right;
  margin-bottom: 10px;

}

.marker-item p {
  margin: 0;
  padding: 5px 0;
}

.marker-item hr {
  margin: 10px 0;
}
</style>
