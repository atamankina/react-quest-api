from fastapi import APIRouter

from app.core.mongo import get_quiz_collection
from app.schemas.quiz import QuizQuestionRead

router = APIRouter(prefix="/quiz-questions", tags=["quiz"])


@router.get("/", response_model=list[QuizQuestionRead])
def get_quiz_questions():
    collection = get_quiz_collection()
    questions = list(collection.find({}, {"_id": 0}))
    return questions
