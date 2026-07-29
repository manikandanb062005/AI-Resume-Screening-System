from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint_returns_running_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ML service running"}


def test_docs_endpoint_is_reachable():
    response = client.get("/docs")
    assert response.status_code == 200


def test_metrics_endpoint_is_reachable():
    response = client.get("/metrics")
    assert response.status_code == 200
    # Prometheus metrics are plain text, not JSON
    assert "http_requests_total" in response.text or "python_info" in response.text


def test_analyze_files_returns_error_when_no_job_description_given():
    # Send a resume file but deliberately omit BOTH job_description_text and job_description_file
    files = {"resumes": ("resume.txt", b"Some resume content", "text/plain")}
    response = client.post("/analyze-files", files=files)
    assert response.status_code == 200
    body = response.json()
    assert "error" in body
