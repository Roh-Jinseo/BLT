import axios from 'axios';

const apiKey = 'sk-proj-COqqur6zYlf1L5TBEeF4T3BlbkFJusZGlUY6ynOGzTPum7vm';  // 실제 API 키로 교체하세요

const instance = axios.create({
    baseURL: 'https://api.openai.com/v1',
    headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
    }
});

export const getChatResponse = async (prompt) => {
    try {
        const response = await instance.post('/completions', {
            model: 'text-davinci-003',
            prompt: prompt,
            max_tokens: 150
        });
        return response.data.choices[0].text.trim();
    } catch (error) {
        console.error('Error fetching chat response:', error.response || error.message);
        throw error;
    }
};

export const generateRecommendationPrompt = (username, financialData, userInfo) => {
    const userDetail = `User Information: Age: ${userInfo.age}, Salary: ${userInfo.salary}, Current Assets: ${userInfo.currentAsset}`;
    const financialProducts = financialData.map(item => item.kor_co_nm).join(', ');

    return `Hello ${username}, based on your age, salary, and current assets, I recommend the following financial products: ${financialProducts}. ${userDetail}.`;
};
