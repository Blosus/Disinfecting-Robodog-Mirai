# syntax=docker/dockerfile:1

# ------------ Imagen Base con CUDA ------------
FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

# ------------ Dependencias del sistema ------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    git \
    libgl1 \
    libglib2.0-0 \
    libusb-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ------------ Dependencias de Python (con cache persistente) ------------
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=600 torch

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=300 opencv-python ultralytics mediapipe pyrealsense2 pyyaml tqdm openni

# ------------ Copiar el proyecto ------------
COPY . .

CMD ["python3", "launchhoi.py"]