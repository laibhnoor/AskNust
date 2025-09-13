// frontend/src/services/api.js
import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // your backend

export async function sendQuery(query) {
  try {
    const response = await axios.post(`${API_URL}/chat`, { query });
    return response.data;
  } catch (error) {
    console.error("Error fetching response:", error);
    return { answer: "⚠️ Backend not reachable!" };
  }
}
