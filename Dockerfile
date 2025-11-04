# Base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git gcc && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest flake8 black ruff joblib

# Run lint + test as a check (optional)
RUN flake8 src && pytest --maxfail=1 --disable-warnings -q || true

# Default command for container
CMD ["python", "src/train.py"]
