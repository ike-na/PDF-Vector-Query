import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const generateAnswer = async (query: string): Promise<string> => {
  try {
    const response = await axios.post(`${API_URL}/generate`, { query });
    return response.data.answer;
  } catch (error) {
    console.error('Error generating answer:', error);
    throw error;
  }
};