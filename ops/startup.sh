#!/bin/bash

# Default to http if not set
SERVICE_TYPE=${SERVICE_TYPE:-"http"}
source .venv/bin/activate
case ${SERVICE_TYPE} in
  "http")
    echo "Starting http service..."
    fastapi run hello.py --no-reload --host 0.0.0.0 --port 85
    ;;
  "grpc")
    echo "Starting gRPC service..."
    python serve.py
    ;;
  *)
    echo "Invalid SERVICE_TYPE: ${SERVICE_TYPE}"
    echo "Running both http and gRPC services..."
    fastapi run hello.py --no-reload --host 0.0.0.0 --port 85 & python serve.py
    ;;
esac