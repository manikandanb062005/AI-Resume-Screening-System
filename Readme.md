# 🚀 AI Resume Screening System

An intelligent **AI-powered Resume Screening Web App** that analyzes multiple resumes against a job description using **Machine Learning + NLP techniques** and ranks candidates automatically.

---

## 📌 Features

* 📄 Upload multiple resumes (PDF, DOCX, TXT)
* 🧠 ML-based resume scoring
* 🔍 Keyword matching analysis
* 🎯 Final candidate ranking
* ⚖️ Bias detection (fair hiring support)
* 🧩 Skill gap analysis (matching & missing skills)
* 📊 Dashboard with score visualization
* 📥 Download Excel report
* ⚡ FastAPI backend + React frontend

---

## 🏗️ Tech Stack

### 🔹 Backend

* **FastAPI**
* **Scikit-learn**
* **XGBoost**
* **Pandas**
* **PyPDF2 / python-docx**

### 🔹 Frontend

* **React.js**
* **Axios**
* **Recharts**
* **Custom CSS (Glass UI)**

---

## 📂 Project Structure

```
AI_Resume_Screening/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   └── pipeline.py
│   │   ├── services/
│   │   │   ├── cleaner.py
│   │   │   ├── similarity.py
│   │   │   ├── skill_gap.py
│   │   │   ├── bias.py
│   │   │   ├── experience.py
│   │   │   ├── file_parser.py
│   │   │   └── report.py
│   │   └── main.py
│   ├── models/
│   │   ├── model.pkl
│   │   └── vectorizer.pkl
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api/
│   │   ├── App.jsx
│   │   └── index.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

👉 Backend runs on:
`http://127.0.0.1:8000`

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

👉 Frontend runs on:
`http://localhost:5173`

---

## 🚀 How It Works

1. Upload resumes (PDF/DOCX/TXT)
2. Enter Job Description
3. Click **Analyze**
4. System performs:

   * Text cleaning
   * Feature extraction (TF-IDF)
   * ML prediction (XGBoost)
   * Keyword matching
   * Skill gap analysis
   * Bias detection
5. Results displayed:

   * Candidate scores
   * Ranking
   * Skills analysis
6. Download Excel report

---

## 📊 Output Example

| Rank | Score | Status   | Role                 |
| ---- | ----- | -------- | -------------------- |
| 1    | 85%   | Selected | Backend ML Developer |
| 2    | 68%   | Consider | Backend Developer    |
| 3    | 23%   | Rejected | Frontend Developer   |

---

## ⚖️ Bias Detection

The system detects potentially biased terms like:

* "young"
* "male"
* "female"
* "age"
* "gender"

Promotes **fair and unbiased hiring decisions**.

---

## 📥 Excel Report

Download a structured report including:

* Rank
* Final Score
* ML Score
* Keyword Score
* Skills Match
* Missing Skills

---

## 🧠 Machine Learning Model

* **Vectorization:** TF-IDF
* **Model:** XGBoost Classifier
* **Training:** Resume dataset with labeled relevance

---

## 🎯 Future Enhancements

* 📄 PDF report generation
* 🌐 Deployment (Render / Vercel)
* 🧾 Resume preview modal
* 📊 Advanced analytics dashboard
* 🤖 GPT-based resume feedback

---

## 👨‍💻 Author

**Manikandan B**

---

## 💬 Project Summary (for Interview)

> Built an AI-powered resume screening system using FastAPI and React that ranks candidates based on ML predictions, keyword matching, and skill gap analysis, with bias detection and Excel report generation.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
