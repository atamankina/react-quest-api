from pydantic import BaseModel


class AnswerOption(BaseModel):
    id: str
    text: str
    isCorrect: bool


class QuizQuestion(BaseModel):
    id: str
    question: str
    answers: list[AnswerOption]
    explanation: str
