from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import create_task, get_tasks, get_task, update_task, delete_task

# Импортируем модель для создания таблицы
import models
Base.metadata.create_all(bind=engine)

# Создаем приложение FastAPI
app = FastAPI()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/")
def create_task_endpoint(title: str, description: str = "", db: Session = Depends(get_db)):
    return create_task(db, title, description)

@app.get("/tasks/")
def get_tasks_endpoint(db: Session = Depends(get_db)):
    return get_tasks(db)

@app.get("/tasks/{task_id}")
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    return get_task(db, task_id)

@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, title: str, completed: bool, db: Session = Depends(get_db)):
    return update_task(db, task_id, title, completed)

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)
