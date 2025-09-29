# Multi-stage build for Python application using uv
FROM python:3.13-slim AS builder

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files for uv
COPY pyproject.toml uv.lock README.md ./

# Install only production dependencies with uv (exclude dev/test dependencies)
RUN uv sync --frozen --no-cache --no-dev

# Copy source
COPY app/ ./app/

# Production stage
FROM python:3.13-slim AS production

# Build arg for version
ARG APP_VERSION=development

WORKDIR /app

# Install curl for health checks
RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN addgroup --gid 1001 --system appuser && \
    adduser --uid 1001 --system --group appuser

# Copy Python environment from builder (uv virtual environment)
COPY --from=builder /app/.venv /app/.venv

# Copy app with correct ownership
COPY --from=builder --chown=appuser:appuser /app/app ./app

# Make sure we use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Environment variables
ENV APP_VERSION=${APP_VERSION}
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Start app
CMD ["python", "app/app.py"]
