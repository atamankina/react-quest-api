from fastapi import APIRouter

from app.core.mongo import get_lessons_collection
from app.schemas.lesson import LessonRead

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=list[LessonRead])
def get_lessons():
    collection = get_lessons_collection()
    lessons = list(collection.find({}, {"_id": 0}))
    return lessons
