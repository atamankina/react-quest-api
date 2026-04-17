from fastapi import APIRouter

from app.services.file_service import read_json
from app.core.config import QUIZ_FILE
from app.models.quiz import QuizQuestion

router = APIRouter(prefix="/quiz-questions", tags=["quiz"])


@router.get("/", response_model=list[QuizQuestion])
def get_quiz_questions():
    return read_json(QUIZ_FILE)
