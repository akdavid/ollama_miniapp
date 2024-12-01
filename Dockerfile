# Base image
FROM python:3.11-slim AS base

# Install dependencies for Python and Node.js
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install supervisord for process management
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy backend requirements and install
COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy frontend dependencies and build the frontend
COPY frontend/package*.json frontend/
RUN cd frontend && npm install && npm run build
COPY ./frontend ./frontend

# Copy Ollama entrypoint and dependencies
COPY ollama/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Copy application code
COPY backend backend
COPY frontend frontend
COPY ollama ollama

# Create supervisord configuration
RUN mkdir -p /etc/supervisor/conf.d
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 8000 8080 11434

# Default command
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
