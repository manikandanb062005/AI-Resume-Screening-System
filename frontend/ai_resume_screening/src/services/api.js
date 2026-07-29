import axios from "axios";

const API = "/api";

export const analyzeFiles = async (formData) => {
  const res = await axios.post(`${API}/analyze-files`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};