from pydantic import BaseModel, Field, conlist, condecimal, constr
from typing import List
from datetime import date

from src.database.models import MovieStatusEnum


class MovieCreateSchema(BaseModel):
    name: str
    date: date
    score: float = Field(..., ge=0.0, le=100.0)
    overview: str
    status: MovieStatusEnum
    budget: float = Field(..., ge=0.0)
    revenue: float = Field(..., ge=0.0)
    country: constr(min_length=3, max_length=3)
    genres: List[str]
    actors: List[str]
    languages: List[str]