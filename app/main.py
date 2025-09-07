from fastapi import FastAPI, APIRouter
from app.interfaces import habit_router

# Crea la estructura principal de FastAPI
app = FastAPI(title="Habit Tracker API", version="0.1.0")

# Crea el Router
router = APIRouter(prefix="/health", tags=["health"])

# Crea el endpoint
@router.get("", summary="Health check")
async def health() -> dict:
    return {"status": "ok"}

# Agrega el router a app
app.include_router(router)
app.include_router(habit_router.router)