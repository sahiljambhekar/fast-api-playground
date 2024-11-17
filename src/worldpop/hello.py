from typing import Dict
from contextlib import asynccontextmanager
from fastapi import FastAPI
from redis_helper import RedisHelper
from time import perf_counter
from models import (
    RandomCityRandomStateResponse,
    RandomCityResponse,
    RandomStateResponse,
    RootReply,
)
from prometheus_fastapi_instrumentator import Instrumentator, metrics


async def setup_redis():
    global redis_helper
    redis_helper = RedisHelper()
    start = perf_counter()
    await redis_helper.startup()
    time_taken = (perf_counter() - start) * 1000
    print(f"Redis startup took {time_taken:.2f}ms")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_redis()
    yield


DEFAULT_BUCKETS = [
    0.0005,
    0.001,
    0.002,
    0.003,
    0.004,
    0.005,
    0.006,
    0.007,
    0.008,
    0.009,
    0.01,
    0.05,
    0.25,
    0.5,
    0.75,
    1.0,
]

app = FastAPI(
    lifespan=lifespan,
    title="Random City Generator",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

instrumentor = Instrumentator(
    should_instrument_requests_inprogress=True,
    excluded_handlers=["admin*", "/metrics", "/docs", "/openapi*"],
)
instrumentor.instrument(app, metric_namespace="fast_api").expose(app)
instrumentor.add(
    metrics.latency(
        metric_name="duration_in_seconds_bucket",
        metric_namespace="fast_api",
        buckets=DEFAULT_BUCKETS,
    )
)
instrumentor.expose(app)


@app.get("/", response_model=RootReply)
def root() -> Dict[str, str]:
    return RootReply(greeting="Hello,there", msg="Welcome, to random city generator!")


@app.get("/state/{state}/random_city", response_model=RandomCityResponse)
async def random_city_by_state(state: str, num: int = 1) -> RandomCityResponse:
    """Get a random city from the specified state.

    Args:
        state (str): The state to get a random city from.
        num (int, optional): The number of random cities to get. Defaults to 1.

    Returns:
        RandomCityResponse: A dictionary with the random city or None.
    """
    result = await redis_helper.get_random_cities(state, num)
    return RandomCityResponse(**result)


@app.get("/cities/random", response_model=RandomCityRandomStateResponse)
async def random_city(num: int = 1) -> RandomCityResponse:
    """Get __num__ random city from a random specified state.

    Args:
        num (int, optional): The number of random cities to get. Defaults to 1.

    Returns:
        RandomCityResponse: A dictionary with the random city or None.
    """
    result = await redis_helper.get_random_cities(num)
    return RandomCityRandomStateResponse(**result)


@app.get("/states/random", response_model=RandomStateResponse)
async def random_state(num: int = 1) -> RandomStateResponse:
    """Get random states from the available states.

    Args:
        num (int, optional): The number of random states to get. Defaults to 1.

    Returns:
        RandomStateResponse: A dictionary with the random states or None.
    """
    result = await redis_helper.get_states(num)
    return RandomStateResponse(**result)
