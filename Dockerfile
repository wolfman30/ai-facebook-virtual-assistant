# Use the official Python 3.11-slim image for a lightweight base
FROM python:3.13-slim

# Set environment variables for Python (production-ready)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies
# Add build-essential and curl for common build tasks
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies with pip
# Use --user for non-root user security and --no-cache-dir to reduce image size
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Add a non-root user for better security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Set the default command to run the application
CMD ["python", "main.py"]
