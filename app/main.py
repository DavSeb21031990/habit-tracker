from fastapi import FastAPI, APIRouter

app = FastAPI(title="Habit Tracker API", version="0.1.0")

router = APIRouter(prefix="/health", tags=["health"])

@router.get("", summary="Health check")
async def health() -> dict:
    return {"status": "ok"}

app.include_router(router)