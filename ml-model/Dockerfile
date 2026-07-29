# ---------- Stage 1: Build dependencies ----------
FROM python:3.11-slim AS builder

WORKDIR /build

# System deps needed to compile some Python packages (numpy, scipy, xgboost wheels etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- Stage 2: Final runtime image ----------
FROM python:3.11-slim

WORKDIR /app

# Create non-root user FIRST, so we can own files by this user as we copy them in
RUN useradd --create-home appuser && chown appuser:appuser /app

# Copy installed packages from builder stage into appuser's home (NOT /root — appuser can't read /root)
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy application code, owned by appuser
COPY --chown=appuser:appuser app/ ./app/
COPY --chown=appuser:appuser train.py .
COPY --chown=appuser:appuser src/ ./src/

# Train the model AT BUILD TIME — bakes model.pkl/vectorizer.pkl into the image
# train.py itself creates ./models/ via os.makedirs("models", exist_ok=True)
# Run as appuser so the resulting models/ folder is owned correctly too
USER appuser
RUN python train.py

EXPOSE 8000

# Basic container-level health check (Kubernetes will also do its own probes later)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/docs')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
