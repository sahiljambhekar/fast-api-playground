# Use an official Python runtime as a parent image
#FROM python:3.10-slim
#FROM ghcr.io/astral-sh/uv:python3.10-alpine
FROM ghcr.io/astral-sh/uv:python3.10-bookworm
# Install build dependencies, for grpc tools
RUN apt-get update && apt-get install -y build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD src/worldpop/ /app/
COPY ops/startup.sh /app/
COPY pyproject.toml /app/

# Install any needed packages specified in requirements.txt
RUN uv sync

# Make port 80 available to the world outside this container for HTTP
# Make port 50051 available to the world outside this container for gRPC
EXPOSE 80 50051

# Run Either HTTP or gRPC server
CMD ["./startup.sh"]
