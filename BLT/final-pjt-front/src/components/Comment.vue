<template>
  <div class="mb-3">
    <template v-if="!comment.editing">
      <p class="mb-1">{{ comment.author.nickname }} : {{ comment.content }}</p>
      <div v-if="comment.author.username === store.saveUsername">
        <button @click="editComment(comment)" type="button" class="btn btn-outline-dark btn-sm">수정하기</button>
        <button @click="store.deleteComment(comment.id)" type="button" class="btn btn-danger btn-sm">삭제하기</button>
      </div>
    </template>
    <template v-else>
      <input v-model="comment.newContent" type="text" class="form-control mb-1">
      <button @click="updateComment(comment)" type="button" class="btn btn-outline-dark btn-sm mr-1">수정 완료</button>
      <button @click="cancelEdit(comment)" type="button" class="btn btn-secondary btn-sm">취소</button>
    </template>
    <button @click="toggleCommentLike(comment, comment.id)" class="btn btn-outline-dark btn-sm">
      {{ isLikedComment ? '좋아요 취소' : '좋아요' }}
    </button>
    <span class="ml-2">좋아요 수: {{ comment.likes_count }}</span>
  </div>
</template>


<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'

const props = defineProps({
                        comment:Object
                      })

// const localComment = ref({ ...props.comment })
const store = useCounterStore()
const isLikedComment = ref(false)


const checkCommentIfLiked = (comment_id) => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/comments/${comment_id}/likes/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      isLikedComment.value = response.data.is_liked
    })
    .catch((error) => {
      console.log(error)
    })
}


const toggleCommentLike = (comment,comment_id) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/comments/${comment_id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {

      checkCommentIfLiked(comment_id)

      // isLikedComment.value = !isLikedComment.value
      if (isLikedComment.value) {
        // 안되면 comment뒤에 value 넣어서 해보기
        comment.likes_count -= 1 
        isLikedComment.value = false
        // event.target.value = '좋아요 취소'
      } else {
        comment.likes_count += 1
        isLikedComment.value = true
        // event.target.value = '좋아요'
      }


    })
    .catch((error) => {
      console.log(error)
    })
}

// 댓글 수정 관련 상태 및 함수
const editComment = function(comment) {
  comment.editing = true
  comment.newContent = comment.content
}

const updateComment = function(comment) {
  store.putComment(comment.id, comment.newContent)
  comment.editing = false
}

const cancelEdit = function(comment) {
  comment.editing = false
}

// 들어오자마자 해당 댓글에 좋아요 했는지 체크
onMounted(()=>{
  checkCommentIfLiked(props.comment.id)
})

</script>

<style scoped>

</style>