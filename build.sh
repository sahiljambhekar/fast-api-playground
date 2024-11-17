#!/bin/bash
export VIRTUAL_ENV=".venv" # uv
# Extract version from pyproject.toml
VERSION=$(yq .project.version pyproject.toml)

docker build . \
-t ghcr.io/sahiljambhekar/fast-api-playground:worldpop-${VERSION} \
-f ops/Dockerfile