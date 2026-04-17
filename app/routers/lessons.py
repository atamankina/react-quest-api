from fastapi import APIRouter

from app.services.file_service import read_json
from app.core.config import LESSONS_FILE
from app.models.lesson import Lesson

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=list[Lesson])
def get_lessons():
    return read_json(LESSONS_FILE)
