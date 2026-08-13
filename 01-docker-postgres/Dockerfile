# Start with slim Python 3.13 image
FROM python:3.13.10-slim

# Copy uv binary from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /code

# Add virtual environment to PATH
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependency files first
COPY pyproject.toml uv.lock .python-version ./

# Install dependencies from lock file
RUN uv sync --locked

# Copy application code
COPY ingest_data.py .
COPY ingest_data2.py .