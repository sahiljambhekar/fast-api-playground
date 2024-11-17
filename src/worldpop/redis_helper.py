## Create a Helper Module/Class which asyncronously connects to Redis and performs operations on it.
## The Redis has HSET with key "state:CA" "stage:AL" and "state:NY" with values as cities in the respective states.
# Path: src/fast/redis_helper.py
import redis.asyncio as redis
from typing import Dict, List, Union
import os
import numpy as np
from utils import measure_time


class RedisHelper:
    def __init__(self) -> None:
        redis_url = os.getenv("REDIS_URL", "redis://localhost")
        print(f"Connecting to Redis at {redis_url}")
        pool = redis.ConnectionPool.from_url(
            redis_url, max_connections=500, decode_responses=True
        )
        self.redis_client = redis.Redis(connection_pool=pool)

    async def startup(self):
        # Warm up the redis connection
        for _ in range(1_000):
            await self.redis_client.ping()

    async def get_random_city(self, state: str, number: int = 1) -> List[str]:
        random_cities = await self.redis_client.srandmember(
            f"state:{state}", number=number
        )
        return random_cities

    async def get_random_state(self, number: int = 1) -> List[str]:
        random_states = await self.redis_client.srandmember("states", number=number)
        return random_states

    @measure_time
    async def get_random_cities_by_state(
        self, state: str, num: int
    ) -> Dict[str, Union[str, list[str]]]:
        random_cities = await self.get_random_city(state, number=num)
        return {"random_city": random_cities}

    @measure_time
    async def get_random_cities(self, num: int) -> Dict[str, Union[str, list[str]]]:
        states = await self.get_random_state(num)
        random_state: str = str(np.random.choice(states))
        random_ciies: list[str] = await self.get_random_city(random_state, num)
        return {"random_cities": random_ciies, "random_state": random_state}

    @measure_time
    async def get_states(self, num: int) -> Dict[str, Union[str, list[str]]]:
        random_states = await self.get_random_state(number=num)
        return {"random_state": random_states}
