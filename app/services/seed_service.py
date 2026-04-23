import json

from app.core.config import LESSONS_FILE, QUIZ_FILE
from app.core.mongo import get_lessons_collection, get_quiz_collection


def seed_lessons():
    collection = get_lessons_collection()

    if collection.count_documents({}) > 0:
        return

    with LESSONS_FILE.open("r", encoding="utf-8") as f:
        lessons = json.load(f)

    collection.insert_many(lessons)


def seed_quiz_questions():
    collection = get_quiz_collection()

    if collection.count_documents({}) > 0:
        return

    with QUIZ_FILE.open("r", encoding="utf-8") as f:
        questions = json.load(f)

    collection.insert_many(questions)
