import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const saveUsername = ref('')
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()
  const userInfo = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const updateArticle = function(articleId, updatedArticleData) {
    
    axios({
      method: 'put',
      url: `${API_URL}/api/v1/articles/${articleId}/`,
      data: updatedArticleData,
      headers: {
        Authorization: `Token ${token.value}`,
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        alert('게시물을 수정하였습니다.')
        router.push({name:'ArticleDetailView',params: { id: articleId }})
      })
      .catch(error => {
        console.log(error)
      })
  }

  const deleteArticle = function(articleId){
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/articles/${articleId}/`,
    })
      .then(response => {
        alert('해당 게시물을 삭제하였습니다.')
        router.push({name:'ArticleView'})
      })
      .catch(error => {
        console.log(error)
      })
  }

  const comments = ref([])
  const getComments = function(article_pk){
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${article_pk}/comments/`,
    })
      .then(response => {
        comments.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const deleteComment = function(comment_pk){
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/comments/${comment_pk}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        alert('댓글 삭제하였습니다.')
        const index = this.comments.findIndex(comment => comment.id === comment_pk)
        if (index !== -1) {
          this.comments.splice(index, 1)
        }
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 여기 나중에 comment에서 put을 받아오도록 쓰기
  const putComment = function(comment_pk, newContent) {
    axios({
      method: 'put',
      url: `${this.API_URL}/api/v1/comments/${comment_pk}/`,
      headers: {
        Authorization: `Token ${this.token}`
      },
      data: {
        content: newContent
      }
    })
      .then(res => {
        const index = this.comments.findIndex(comment => comment.id === comment_pk)
        if (index !== -1) {
          this.comments[index].content = newContent
        }
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 여기부터는 유저

  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username, password1, password2, email, age, salary, currentAsset, firstName, lastName, gender, nickname } = payload
    // console.log(payload)


    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: username,
        // password1: password1,
        // password2: password2
        username, password1, password2, email, age, salary, currentAsset, 
        first_name: firstName, last_name: lastName, 
        gender, nickname
        //, profile_img
      }
      
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
      //  logIn({ username, password })
        router.push({ name : 'LogInView' })
     })
     .catch((error) => {
        console.log(username, password1, password2, email, age, salary, currentAsset, firstName, lastName, gender,nickname)
        console.log(error)
        // alert(error.response.data)
        alert('제대로 입력하세요./..')
     })
  }

  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response.data)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        saveUsername.value = username
        getUserInfo()
        return response
      })
      .then((response)=> {
        router.push({ name : 'MainView' })
        // console.log(saveUsername.value)
        // console.log('유저네임을찾아서')
      })
      .catch((error) => {
        console.log(error)
      })
  }



  const logout = function(){
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      // data: {
      //   title: title.value,
      //   content: content.value
      // },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        token.value = null
        saveUsername.value=''
        userInfo.value=null
        console.log('로그아웃 됨!')

        alert('로그아웃 성공!')
        // router.push({ name: 'LoginView' })
      })
      .catch((error) => {
        console.log(error)
      })
    
  }


  const getUserInfo = function(){
        axios({
          //img -> django에서 요청해서 가져오기
        method: 'get',
        url: `${API_URL}/accounts/user/`,

        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then(res =>{
        // 유저인포 저장
        userInfo.value = res.data
      })
      .catch(err => console.log(err))
      }


  const unregister = function(username){
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/update/${username}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then((res) => {
        localStorage.removeItem(token.value);
        token.value = null
        saveUsername.value=''
        userInfo.value=null
        alert('지금까지 이용해주셔서 감사합니다.')
        router.push({ name: "LogInView"})
      })
      .catch((err) => console.log(err))
  }


  return { articles, API_URL, getArticles,updateArticle,deleteArticle,getComments,comments,deleteComment,putComment,
    signUp, logIn, token, isLogin, logout, saveUsername, userInfo,getUserInfo,unregister }
}, { persist: true })
