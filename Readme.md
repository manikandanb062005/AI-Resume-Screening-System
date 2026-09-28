# 🚀 AI Resume Screening System — with Full DevOps & CI/CD Pipeline on AWS

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React_19-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white" alt="Helm" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins" />
  <img src="https://img.shields.io/badge/AWS_EKS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
</p>

An enterprise-grade **AI-powered Resume Screening and Candidate Ranking Web Application** backed by Machine Learning (TF-IDF + XGBoost) and NLP techniques, accompanied by a production-ready **Cloud & DevOps Pipeline**: Docker multi-stage builds, Kubernetes orchestrations, Helm packaging, GitHub Actions CI, Jenkins CD with manual approval gates, Prometheus/Grafana monitoring, and AWS Cloud (EKS, ECR, CloudWatch) integration.

---

## 📌 Key Application Features

- 📄 **Multi-Format Parsing:** Seamlessly processes resume files in **PDF**, **DOCX**, and **TXT** formats.
- 🧠 **Machine Learning Scoring:** Predicts candidate-to-job relevance using a trained **XGBoost Classifier** over **TF-IDF n-gram vectors**.
- 🔍 **Keyword & Semantic Matching:** Computes lexical and semantic overlap between candidate profiles and job requirements.
- 🎯 **Automated Ranking:** Automatically calculates normalized scores and assigns clear qualification statuses (*Selected*, *Consider*, *Rejected*).
- ⚖️ **Fairness & Bias Detection:** Identifies potentially biased keywords (e.g., age, gender indicators) to assist unbiased hiring.
- 🧩 **Skill Gap Analysis:** Extracts matched competencies and highlights missing skills required for the role.
- 📊 **Interactive Analytics Dashboard:** Real-time visual metrics, score distributions, and candidate comparison charts powered by **Recharts**.
- 📥 **Automated Report Generation:** One-click generation and download of structured **Excel (.xlsx)** screening summaries.

---

## 🏗️ Technical Architecture & Stack

### 🔹 Backend & Machine Learning
* **Language & Framework:** Python 3.11, FastAPI, Uvicorn
* **ML & NLP Engine:** Scikit-learn, XGBoost Classifier, TF-IDF Vectorizer (1-2 ngrams), Pandas, NumPy
* **Document Parsing:** PyPDF2, python-docx
* **Reporting & Observability:** OpenPyXL, Prometheus FastAPI Instrumentator

### 🔹 Frontend
* **Framework & Tooling:** React 19, Vite, Axios
* **Data Visualization:** Recharts, Lucide React, Framer Motion
* **UI/UX Design:** Glassmorphic modern CSS & Tailwind CSS styling

### 🔹 DevOps, Cloud & Infrastructure
* **Containerization:** Docker (multi-stage non-root builds), Docker Compose
* **Orchestration & Packaging:** Kubernetes (Deployments, Services, NodePort), Helm v3 Charts
* **CI/CD Pipelines:** GitHub Actions (Automated testing, linting, Docker Hub publishing), Jenkins (Image staging, Kind loading, manual approval gates, zero-downtime rolling updates)
* **Cloud Platform (AWS):** Amazon EKS (Elastic Kubernetes Service), Amazon ECR (Elastic Container Registry), AWS CloudWatch (Control plane & Container Insights), eksctl
* **Monitoring & Alerting:** Prometheus, Grafana dashboards, Alertmanager (`HighErrorRate`, `BackendDown` rules), Prometheus Operator ServiceMonitors

---

## 🔄 End-to-End DevOps Workflow

```
 Developer Commit & Push
           │
           ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                    GitHub Actions (CI)                      │
 │  • Backend: Pytest Unit Tests (9/9 passed) + Model Training │
 │  • Frontend: ESLint Code Quality Checks + Vite Build        │
 │  • Containerization: Docker Buildx Multi-stage Build        │
 │  • Registry Push: Automated push to Docker Hub / Amazon ECR │
 └─────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                        Jenkins (CD)                         │
 │  • Pull latest images from container registry               │
 │  • Load images into Kubernetes Cluster (Kind / EKS)         │
 │  • 🛑 Interactive Manual Approval Gate                      │
 │  • Execute zero-downtime rolling deployment (`kubectl`)     │
 └─────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                Kubernetes Runtime Environment               │
 │  • Backend Deployment (FastAPI, 8000)                       │
 │  • Frontend Deployment (Nginx Reverse Proxy, 8080)          │
 │  • Liveness & Readiness Health Probes                       │
 └─────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
 ┌─────────────────────────────────────────────────────────────┐
 │             Observability & Production Monitoring           │
 │  • Prometheus scrapes `/metrics` endpoint every 15s         │
 │  • Grafana Dashboard: Latency (P95), Request Rates, Errors  │
 │  • Alertmanager: Configured for SLA breaches & downtime     │
 │  • AWS CloudWatch: Container Insights & cluster logs        │
 └─────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
Ai_ResumeScreening/
├── .github/workflows/          # Automated GitHub Actions CI Pipelines
│   ├── backend-ci.yml          # Backend test, build, and container push
│   └── frontend-ci.yml         # Frontend lint, bundle, and container push
├── Jenkinsfile                 # Jenkins CD Pipeline with approval gates
├── docker-compose.yml          # Local multi-service composition (Backend + Frontend)
├── kind-config.yaml            # Local Kubernetes Kind cluster definition
├── eks-cluster.yaml            # Production AWS EKS cluster spec (eksctl)
├── resume-screening-chart/     # Production Helm Chart
│   ├── Chart.yaml              # Chart metadata
│   ├── values.yaml             # Configurable deployment values
│   └── templates/              # Kubernetes manifest templates
├── monitoring/                 # Observability resources
│   ├── backend-servicemonitor.yaml  # Prometheus Operator ServiceMonitor
│   └── backend-alerts.yaml          # Alertmanager Prometheus rules
├── k8s/                        # Raw standalone Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
├── ml-model/                   # FastAPI Backend & Machine Learning Service
│   ├── app/
│   │   ├── api/routes.py       # API endpoints (/analyze-files, /download-report)
│   │   ├── core/pipeline.py    # Resume processing and scoring pipeline
│   │   ├── services/           # Text cleaner, similarity, bias, skill gap
│   │   └── main.py             # FastAPI entrypoint & CORS middleware
│   ├── tests/                  # Pytest test suite
│   │   ├── test_cleaner.py
│   │   └── test_routes.py
│   ├── models/                 # Serialized model and TF-IDF vectorizer (.pkl)
│   ├── src/                    # Dataset for model training
│   ├── train.py                # Model training and hyperparameter tuning script
│   ├── Dockerfile              # Non-root multi-stage Python build
│   └── requirements.txt        # Backend dependencies
└── frontend/ai_resume_screening/  # React 19 Frontend Web Application
    ├── src/
    │   ├── components/         # Dashboard, DropZone, ResultsGrid, Modals
    │   ├── services/api.js     # Axios API client
    │   ├── App.jsx             # Main application state and views
    │   └── index.css           # Custom styling
    ├── nginx.conf              # Nginx production reverse proxy configuration
    ├── Dockerfile              # Multi-stage Node build & Nginx runtime
    ├── package.json            # Frontend package manifest
    └── vite.config.js          # Vite configuration with development API proxy
```

---

## ⚙️ Getting Started & Running Locally

### Option 1: Quick Start with Docker Compose (Recommended)

Run the full multi-container stack with a single command:

```bash
docker compose up -d --build
```

Access the services:
* **Web UI:** [http://localhost:8080](http://localhost:8080)
* **FastAPI Interactive Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Metrics Endpoint:** [http://localhost:8000/metrics](http://localhost:8000/metrics)

---

### Option 2: Local Kubernetes Deployment (Kind + Helm)

Deploy using the parameterized Helm chart on a local Kind cluster:

```bash
# 1. Create local Kind cluster with port mapping (30080 -> 8080)
kind create cluster --config kind-config.yaml

# 2. Build local Docker images
docker build -t resume-backend:local ./ml-model
docker build -t resume-frontend:local ./frontend/ai_resume_screening

# 3. Load images into the Kind cluster
kind load docker-image resume-backend:local --name resume-screening
kind load docker-image resume-frontend:local --name resume-screening

# 4. Install via Helm
helm install resume-screening ./resume-screening-chart \
  --set backend.image.repository=resume-backend \
  --set backend.image.tag=local \
  --set frontend.image.repository=resume-frontend \
  --set frontend.image.tag=local
```

Access the application at [http://localhost:8080](http://localhost:8080).

---

### Option 3: Local Developer Setup (Bare Metal)

#### Backend Setup
```bash
cd ml-model
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
pip install -r requirements.txt

# Train model (required before first run)
python train.py

# Start FastAPI server
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

#### Frontend Setup
```bash
cd frontend/ai_resume_screening
npm install
npm run dev
```

The frontend will run at `http://localhost:5173` with automatic API proxying to port 8000.

---

## 🧪 Automated Testing & Code Quality

### Backend Unit Tests
```bash
cd ml-model
pytest -v
```
* **Coverage:** Validates text sanitization, resume file parsing (PDF/DOCX/TXT), TF-IDF feature mapping, XGBoost scoring, bias detection, and FastAPI route responses.

### Frontend Linting & Build Verification
```bash
cd frontend/ai_resume_screening
npm run lint
npm run build
```

---

## 📈 Monitoring & Observability

The application is instrumented with **Prometheus FastAPI Instrumentator** and monitored using Prometheus, Grafana, and Alertmanager.

1. **ServiceMonitor Integration:** [`monitoring/backend-servicemonitor.yaml`](./monitoring/backend-servicemonitor.yaml) instructs Prometheus Operator to scrape `/metrics` every 15 seconds.
2. **Prometheus Alerting Rules:** [`monitoring/backend-alerts.yaml`](./monitoring/backend-alerts.yaml) sets automated alerts:
   - `HighErrorRate`: Triggers if HTTP 5xx error rate exceeds 5% over 1 minute.
   - `BackendDown`: Triggers if backend instance is unreachable for >1 minute.
3. **Port Forwarding Dashboards:**
   ```bash
   kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
   kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090
   kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-alertmanager 9093:9093
   ```

---

## ☁️ AWS Cloud Infrastructure & Deployment

> [!NOTE]
> **Cost Management Note:** The production Amazon EKS cluster (`ap-south-1`) and Amazon ECR container registries were provisioned, tested, and validated with real workloads, and subsequently torn down to prevent recurring AWS infrastructure costs. The entire cloud setup is fully reproducible using the provided configuration files.

### Deploying to AWS EKS:
```bash
# 1. Provision Amazon EKS cluster with 2x t3.small worker nodes
eksctl create cluster -f eks-cluster.yaml

# 2. Authenticate Docker with Amazon ECR
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com

# 3. Tag and push container images to ECR
docker tag resume-backend:latest <AWS_ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/resume-backend:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/resume-backend:latest

docker tag resume-frontend:latest <AWS_ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/resume-frontend:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/resume-frontend:latest

# 4. Deploy application stack using Helm
helm install resume-screening ./resume-screening-chart
```

---

## 👨‍💻 Author

**Manikandan B**  
GitHub: [@manikandanb062005](https://github.com/manikandanb062005)

---

## ⭐ Star the Repository
If you found this project helpful or insightful for your DevOps and ML journey, please consider giving it a ⭐ on GitHub!
