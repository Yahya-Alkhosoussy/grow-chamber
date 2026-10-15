# syntax=docker/dockerfile:1

# Use 'slim' instead of 'alpine' for compatibility with pre-compiled wheels
FROM python:3.12-slim

# Set the working directory
WORKDIR /code

# Install system dependencies required by OpenCV (libglib and libgl1 are common)
# Even with 'slim', headless OpenCV sometimes needs these system libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
# This will now pull the pre-compiled .whl files instead of building from source
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

CMD ["python3", "-u", "app.py"]