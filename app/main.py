from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import FRONTEND_ORIGIN
from app.routers import lessons, quiz


app = FastAPI(title="React Quest API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(lessons.router)
app.include_router(quiz.router)

@app.get("/")
def read_root():
    return {"message": "React Quest API is running."}
