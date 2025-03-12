# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    vim \
    python3-pip \
    python3-dev \
    python3-opencv \
    libopencv-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    xvfb \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt /app/
RUN pip install --timeout=180 -r requirements.txt

# Copy all project files
COPY . .

# Set environment variable for display
ENV DISPLAY=:99

# Start Xvfb
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & exec bash"]

