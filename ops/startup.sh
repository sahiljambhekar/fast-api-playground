#!/bin/bash

# Default to http if not set
SERVICE_TYPE=${SERVICE_TYPE:-"http"}
source .venv/bin/activate
case ${SERVICE_TYPE} in
  "http")
    echo "Starting http service..."
    fastapi run hello.py --no-reload --host 0.0.0.0 --port 85
    ;;
  "hyper")
    echo "Starting http1.1 service with hypercorn..."
    hypercorn hello:app --bind 0.0.0.0:85 --log-level=critical
    #fastapi run hello.py --no-reload --host 0.0.0.0 --port 85
    ;;
  "grpc")
    echo "Starting gRPC service..."
    python serve.py
    ;;
  *)
    echo "Invalid SERVICE_TYPE: ${SERVICE_TYPE}"
    echo "Running both http1.1 and gRPC services..."
    fastapi run hello.py --no-reload --host 0.0.0.0 --port 85 & python serve.py
    ;;
esac