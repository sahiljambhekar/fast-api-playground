from pydantic import BaseModel
from typing import List


class RandomCityResponse(BaseModel):
    random_city: List[str]
    time_taken: str


class RandomCityRandomStateResponse(BaseModel):
    random_cities: List[str]
    random_state: str
    time_taken: str


class RandomStateResponse(BaseModel):
    random_state: List[str]
    time_taken: str


class RootReply(BaseModel):
    greeting: str
    msg: str
