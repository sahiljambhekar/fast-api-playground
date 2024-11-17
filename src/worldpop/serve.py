import asyncio
import grpc
from pb.random_city_pb2 import RandomCityRequest, RandomCityResponse
from pb.random_city_pb2_grpc import (
    RandomCityServiceServicer,
    add_RandomCityServiceServicer_to_server,
)
from redis_helper import RedisHelper


class RandomCityService(RandomCityServiceServicer):
    def __init__(self):
        self.redis_helper = RedisHelper()

    async def startup(self):
        await self.redis_helper.startup()

    async def GetRandomCity(
        self, request: RandomCityRequest, context: grpc.aio.ServicerContext
    ) -> RandomCityResponse:
        result = await self.redis_helper.get_random_cities(request.num)
        return RandomCityResponse(
            random_cities=result["random_cities"],
            random_state=result["random_state"],
            time_taken=result["time_taken"],
        )


async def serve():
    server = grpc.aio.server()
    service = RandomCityService()
    await service.startup()
    add_RandomCityServiceServicer_to_server(service, server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
