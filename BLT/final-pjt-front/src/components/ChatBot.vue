<template>
  <div class="chatbot">
    <div class="messages">
      <div v-for="message in messages" :key="message.id" :class="message.type">
        {{ message.text }}
      </div>
    </div>
    <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message here..." />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useProductStore } from '@/stores/product';
import { useCounterStore } from '@/stores/counter';
import { getChatResponse, generateRecommendationPrompt } from '../openai';

const messages = ref([]); // 채팅 메시지 배열
const userInput = ref(''); // 사용자 입력값

const productStore = useProductStore();
const counterStore = useCounterStore();

// 채팅 전송 함수
const sendMessage = async () => {
  if (userInput.value.trim() === '') return; // 빈 입력일 경우 처리하지 않음

  // 사용자 메시지 추가
  const userMessage = { id: Date.now(), text: userInput.value, type: 'user' };
  messages.value.push(userMessage);

  // 챗봇 응답 가져오기
  let botResponse = '';
  try {
    botResponse = await getBotResponse(userInput.value); // 챗봇 응답 받아오기
  } catch (error) {
    botResponse = 'Sorry, there was an error processing your request. Please try again later.'; // 에러 처리
  }

  // 챗봇 응답 추가
  const botMessage = { id: Date.now() + 1, text: botResponse, type: 'bot' };
  messages.value.push(botMessage);

  userInput.value = ''; // 입력값 초기화


    // 채팅창 스크롤 이동
  const chatContainer = document.querySelector('.messages');
  chatContainer.scrollTop = chatContainer.scrollHeight;
};

// // 챗봇 응답을 가져오는 함수
// const getBotResponse = async (message) => {
//   // 'recommend' 키워드가 포함된 경우에는 추천 메시지 생성
//   if (message.toLowerCase().includes('recommend')) {
//     const prompt = generateRecommendationPrompt(counterStore.saveUsername, productStore.depositOptionCombine, counterStore.userInfo);
//     return await getChatResponse(prompt);
//   } else {
//     // 그 외의 경우에는 직접 사용자 메시지를 전달
//     return await getChatResponse(message);
//   }
// };


// 챗봇 응답을 가져오는 함수
const getBotResponse = async (message) => {
  try {
    if (!message) throw new Error('Empty message'); // 빈 메시지인 경우 에러 발생

    // 'recommend' 키워드가 포함된 경우에는 추천 메시지 생성
    if (message.toLowerCase().includes('recommend')) {
      const prompt = generateRecommendationPrompt(counterStore.saveUsername, productStore.depositOptionCombine, counterStore.userInfo);
      return await getChatResponse(prompt);
    } else {
      // 그 외의 경우에는 직접 사용자 메시지를 전달
      return await getChatResponse(message);
    }
  } catch (error) {
    console.error(error); // 에러 로깅
    return 'Sorry, there was an error processing your request. Please try again later.'; // 에러 메시지 반환
  }
};




</script>


<style scoped>
.chatbot {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.messages {
  max-height: 400px;
  overflow-y: auto;
  margin-bottom: 20px;
}
.user {
  text-align: right;
  color: blue;
}
.bot {
  text-align: left;
  color: green;
}
input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
