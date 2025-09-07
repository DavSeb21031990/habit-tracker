from pydantic import BaseModel, Field, validator, field_validator
from datetime import date
import re


class Habit(BaseModel):
    id: str = Field(..., min_length=2, max_length=50)
    name: str = Field(..., min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=250)
    frequency: str = Field(..., pattern="^(daily|weekly|monthly)$")
    start_date: date

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not re.match(r"^[A-Za-z0-9\s]+$", v):
            raise ValueError("Name must contain only letters, numbers and spaces")
        return v