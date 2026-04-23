from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import FRONTEND_ORIGIN
from app.core.db import Base, engine

from app.models import LessonDB, QuizQuestionDB, AnswerOptionDB
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


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "React Quest API is running."}
