# Build stage
FROM ghcr.io/astral-sh/uv:python3.10-bookworm AS builder

WORKDIR /app
COPY pyproject.toml /app/
RUN uv sync 

FROM python:3.10-slim-bookworm AS runtime
# Copy the app from the builder stage
COPY --from=builder /app /app

WORKDIR /app

ADD src/worldpop/ /app/
ADD config/*.toml /app/config/
COPY ops/startup.sh /app/

EXPOSE 85 50051

CMD ["./startup.sh"]
