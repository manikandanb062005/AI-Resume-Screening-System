import axios from "axios";

const API = "http://127.0.0.1:8000";

export const analyzeFiles = async (formData) => {
  const res = await axios.post(`${API}/analyze-files`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};