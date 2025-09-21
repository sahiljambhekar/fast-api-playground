# fast-api-playground

Just playing around with FastAPI based on their Docs, to see how fast can it be?

## 🚀 How to Run This FastAPI Project

### 1. Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/) (for containerized setup)

---

### 2. Install uv (Recommended)

On macOS/Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
brew install uv
```

---

### 3. Install Python Dependencies

```sh
uv sync
```

This will install all dependencies as specified in `pyproject.toml` and lock them with `uv.lock`.

---

### 4. Run Redis (Locally)

You can run Redis using Docker **or** natively on your Mac:

#### **Option 1: Docker (Recommended)**

```sh
docker run -d -p 6379:6379 redis:latest
```

#### **Option 2: Docker Compose**

From the `ops` directory:

```sh
cd ops
docker compose up redis
```

#### **Option 3: Native Install (Homebrew)**

If you prefer to install Redis directly:

```sh
brew install redis
brew services start redis
```

Or run it manually:

```sh
redis-server
```

You can check if Redis is running with:

```sh
redis-cli ping
```

A running server will reply with `PONG`.

---

### 5. Run the FastAPI App (Development)

From the project root:

```sh
cd src/worldpop
fastapi dev hello.py
# or for production mode
fastapi run hello.py --host 0.0.0.0 --port 85
```

The API will be available at [http://localhost:85/docs](http://localhost:85/docs)

---

### 6. Run with Hypercorn (HTTP/1.1, HTTP/2, etc)

```sh
cd src/worldpop
hypercorn hello:app --config ../../config/hypercorn_config.toml
```

---

### 7. Run Everything with Docker Compose

This project includes a `docker-compose.yml` for local development and testing.

```sh
cd ops
docker compose up --build
```

This will start:

- The FastAPI app (via Hypercorn)
- Redis

The app will be available at [http://localhost:8085/docs](http://localhost:8085/docs)

---

### 8. Custom Service Types

You can control which service runs (http, hyper, grpc) by setting the `SERVICE_TYPE` environment variable:

```sh
# Example: run HTTP/1.1 with Hypercorn
SERVICE_TYPE=hyper ./ops/startup.sh
```

---

### 9. Useful Commands

- **Build Docker image:**

 ```sh
 cd ops
 docker build -t fast-api-playground .
 ```

- **Stop all containers:**

 ```sh
 docker compose down
 ```

---

### 10. Access API Docs

- Local: [http://localhost:85/docs](http://localhost:85/docs)
- Docker Compose: [http://localhost:8085/docs](http://localhost:8085/docs)

---

### References

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [uv Docs](https://astral.sh/uv/)
- [Hypercorn Docs](https://pgjones.gitlab.io/hypercorn/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Redis Docs](https://redis.io/)

---

### Evaluations

See [How Fast](./docs/how-fast.md)
