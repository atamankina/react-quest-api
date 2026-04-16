from fastapi import FastAPI

from app.routers import lessons, quiz


app = FastAPI(title="React Quest API")

app.include_router(lessons.router)
app.include_router(quiz.router)

@app.get("/")
def read_root():
    return {"message": "React Quest API is running."}
