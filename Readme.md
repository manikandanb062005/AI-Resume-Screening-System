# 🚀 AI Resume Screening System — with Full CI/CD Pipeline on AWS

An AI-powered resume screening web app (FastAPI + React + ML) with a complete
production-style DevOps pipeline: Docker, Kubernetes, Helm, GitHub Actions, Jenkins,
Prometheus/Grafana/Alertmanager, and AWS (ECR, EKS, CloudWatch).

---

## 📌 Application Features

- 📄 Upload multiple resumes (PDF, DOCX, TXT)
- 🧠 ML-based resume scoring (TF-IDF + XGBoost)
- 🔍 Keyword matching analysis
- 🎯 Final candidate ranking
- ⚖️ Bias detection (fair hiring support)
- 🧩 Skill gap analysis (matching & missing skills)
- 📊 Dashboard with score visualization
- 📥 Download Excel report

## 🏗️ Application Tech Stack

**Backend:** FastAPI, Scikit-learn, XGBoost, Pandas, PyPDF2, python-docx
**Frontend:** React 19, Vite, Axios, Recharts, Tailwind CSS

---

## ⚙️ DevOps Pipeline — What This Project Demonstrates

```
Developer
   │  git push
   ▼
GitHub Actions (CI)
   │  pytest / eslint+build → docker build → push to Docker Hub & ECR
   ▼
Jenkins (CD)
   │  pull image → load into cluster → MANUAL APPROVAL → deploy via Helm
   ▼
Kubernetes (kind locally / Amazon EKS in prod)
   │  Deployments + Services for backend & frontend
   ▼
Prometheus + Grafana + Alertmanager
   │  scrape /metrics → custom dashboard → alert rules → PROVEN via real triggered outage
   ▼
AWS CloudWatch
      EKS control-plane logs + Container Insights
```

### Technologies used
Linux · Git/GitHub · GitHub Actions · Jenkins · Docker · Docker Compose ·
Amazon EC2/ECR/EKS · Kubernetes · kubectl · Helm · Prometheus · Grafana ·
Alertmanager · AWS IAM/VPC/CloudWatch

---

## 📂 Project Structure

```
AI_Resume_Screening/
├── .github/workflows/          # CI pipelines (backend + frontend)
│   ├── backend-ci.yml
│   └── frontend-ci.yml
├── Jenkinsfile                 # CD pipeline with manual approval gate
├── docker-compose.yml          # Local multi-container dev
├── kind-config.yaml            # Local Kubernetes cluster config
├── eks-cluster.yaml            # AWS EKS cluster config (eksctl)
├── resume-screening-chart/     # Helm chart (backend + frontend)
│   ├── values.yaml
│   └── templates/
├── monitoring/                 # Prometheus ServiceMonitor + alert rules
│   ├── backend-servicemonitor.yaml
│   └── backend-alerts.yaml
├── k8s/                        # Reference raw manifests
├── ml-model/                   # FastAPI backend + ML pipeline
│   ├── app/                    # main.py, api/, core/, services/
│   ├── tests/                  # pytest suite
│   ├── train.py
│   ├── Dockerfile
│   └── requirements.txt
└── frontend/ai_resume_screening/  # React frontend
    ├── src/
    ├── Dockerfile
    └── nginx.conf
```

---

## ⚙️ Local Setup

### Run everything with Docker Compose
```bash
docker compose up -d --build
```
- Frontend: http://localhost:8080
- Backend docs: http://localhost:8000/docs

### Run on local Kubernetes (kind)
```bash
kind create cluster --config kind-config.yaml
kind load docker-image resume-backend:local --name resume-screening
kind load docker-image resume-frontend:local --name resume-screening
helm install resume-screening resume-screening-chart/
```
App available at http://localhost:8080

### Backend tests
```bash
cd ml-model
python train.py     # required first — model loads at import time
pytest -v
```

---

## 📊 Monitoring

- **Prometheus**: scrapes custom `/metrics` from the backend (request rate, latency, error rate)
- **Grafana dashboard** "Resume Screening - Application Metrics": Request Rate by Endpoint,
  P95 Latency, Error Rate (%), Total Requests Processed
- **Alertmanager**: `HighErrorRate` (>5% for 1min) and `BackendDown` (target absent for 1min)
  — both verified by deliberately triggering a real outage and confirming the alert fired

```bash
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-alertmanager 9093:9093
```

---

## 🔄 CI/CD

- **GitHub Actions**: on every push, runs tests (pytest / eslint+build), then builds and
  pushes Docker images to Docker Hub and Amazon ECR
- **Jenkins**: pulls the latest image, loads it into the cluster, **pauses for manual
  approval**, then deploys via `kubectl rollout restart` and verifies the rollout

---

## ☁️ AWS Deployment

Deployed to a real **Amazon EKS** cluster (2× t3.small nodes, ap-south-1) using the
same Helm chart as local development — no manifest changes required between local
`kind` and production EKS. Images pulled from **Amazon ECR**. Logs and metrics sent
to **CloudWatch** (control-plane logging + Container Insights).

> The EKS cluster is torn down between demos to avoid ongoing AWS costs. See
> `eks-cluster.yaml` to recreate it, and the commands below to redeploy.

```bash
eksctl create cluster -f eks-cluster.yaml
helm install resume-screening resume-screening-chart/
```

---

## 🧠 Machine Learning

- **Vectorization:** TF-IDF
- **Model:** XGBoost Classifier
- **Training:** Resume dataset with labeled relevance, trained at Docker build time
  for reproducible, ready-to-serve images

---

## ⚖️ Bias Detection

Flags potentially biased terms (e.g. "young", "male", "female", "age", "gender")
to support fair, unbiased hiring decisions.

---

## 👨‍💻 Author

**Manikandan B**
GitHub: [manikandanb062005](https://github.com/manikandanb062005)

---

## ⭐ If you like this project, give it a star on GitHub!
