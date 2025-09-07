from fastapi import APIRouter
from datetime import date
from app.domain.habit import Habit

router = APIRouter(prefix="/habits", tags=["habits"])

@router.get("/sample", response_model=Habit)
async def getr_sample_habit():
    return Habit(
        id="h1",
        name="Read 30min",
        description="Daily reading habit",
        frequency="daily",
        start_date=date.today()
    )