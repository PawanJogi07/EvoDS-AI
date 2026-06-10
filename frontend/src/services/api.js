import axios from "axios";

const API = axios.create({
  baseURL: "https://evods-ai-1.onrender.com"
});

export default API;
