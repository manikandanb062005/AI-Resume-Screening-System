import axios from "axios";

export const API_BASE = import.meta.env.VITE_API_URL
  ? import.meta.env.VITE_API_URL.replace(/\/$/, "")
  : "/api";

export const analyzeFiles = async (formData) => {
  const res = await axios.post(`${API_BASE}/analyze-files`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};

export const downloadReport = async (results) => {
  const res = await axios.post(`${API_BASE}/download-report`, results, {
    headers: {
      "Content-Type": "application/json",
    },
    responseType: "blob",
  });
  return res.data;
};