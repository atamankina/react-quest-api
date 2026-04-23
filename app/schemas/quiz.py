from pydantic import BaseModel


class AnswerOptionRead(BaseModel):
    id: str
    text: str
    isCorrect: bool


class QuizQuestionRead(BaseModel):
    id: str
    question: str
    answers: list[AnswerOptionRead]
    explanation: str
