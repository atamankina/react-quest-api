from pydantic import BaseModel


class Lesson(BaseModel):
    id: str
    title: str
    topic: str
    type: str
    level: str
    content: str
