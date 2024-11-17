# Use an official Python runtime as a parent image
#FROM python:3.10-slim
#FROM ghcr.io/astral-sh/uv:python3.10-alpine
FROM ghcr.io/astral-sh/uv:python3.10-bookworm
# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY fast/*.py /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN uv pip install --system -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["fastapi", "run","hello.py","--no-reload","--host", "0.0.0.0", "--port", "85"]
