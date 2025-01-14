from sqlalchemy.orm import Session
from models import Task
from fastapi import HTTPException

# Создание новой задачи
def create_task(db: Session, title: str, description: str = ""):
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Получение списка всех задач
def get_tasks(db: Session):
    return db.query(Task).all()

# Получение задачи по ID
def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Обновление задачи по ID
def update_task(db: Session, task_id: int, title: str, completed: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = title
    task.completed = completed
    db.commit()
    db.refresh(task)
    return task

# Удаление задачи по ID
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
