from uuid import UUID
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from backend.models import TodoTask
from backend.schemas import TaskRead, Task, TaskUpdate
from backend.core.db import get_session, Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/task", response_model=TaskRead)
def create_task(task: Task, session=Depends(get_session)):
    try:
        new_task = TodoTask(
            name=task.name, description=task.description, priority=task.priority
        )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.get("/task/{id}", response_model=TaskRead)
def get_task(id: UUID, session=Depends(get_session)):
    try:
        task = session.query(TodoTask).filter(TodoTask.id == id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="task not found!"
            )
        return task

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.get("/tasks", response_model=List[TaskRead])
def get_all_tasks(session=Depends(get_session)):
    try:
        all_tasks = session.query(TodoTask).all()
        return all_tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.patch("/task/{id}", response_model=TaskRead)
def update_task(id: UUID, updated_task: TaskUpdate, session=Depends(get_session)):
    try:
        task = session.query(TodoTask).filter(TodoTask.id == id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="task not found!"
            )
        task.name = updated_task.name if updated_task.name is not None else task.name
        task.description = (
            updated_task.description
            if updated_task.description is not None
            else task.description
        )
        task.priority = (
            updated_task.priority
            if updated_task.priority is not None
            else task.priority
        )

        session.commit()
        session.refresh(task)
        return task

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.delete("/task/{id}")
def delete_task(id: UUID, session=Depends(get_session)):
    try:
        task = session.query(TodoTask).filter(TodoTask.id == id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="task not found!"
            )

        session.delete(task)
        session.commit()
        return {"message": f"{task.id} deleted successfully!"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
