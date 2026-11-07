from fastapi import FastAPI
from routes.tasks import router as task_router

app = FastAPI()

app.include_router(task_router)

@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API"}