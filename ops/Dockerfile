# Build stage
FROM ghcr.io/astral-sh/uv:python3.10-bookworm AS builder
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY pyproject.toml /app/

RUN uv sync

# Runtime stage
FROM ghcr.io/astral-sh/uv:python3.10-alpine

# For Python C++ dependencies
RUN apk add gcc musl-dev
WORKDIR /app

COPY --from=builder /app /app
ADD src/worldpop/ /app/
ADD config/*.toml /app/config/
COPY ops/startup.sh /app/

EXPOSE 85 50051

CMD ["./startup.sh"]
