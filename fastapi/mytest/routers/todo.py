from fastapi import APIRouter
from fastapi import Path
from fastapi import HTTPException
import schemas.todo as todo_schema
from schemas.todo import todos
from typing import List

router = APIRouter(tags=["todos"])


@router.get(path="/todos", response_model=List[todo_schema.Todo])
async def get_todos():
    return todos


@router.post("/todos")
async def create_todo(todo: todo_schema.Todo):
    for node in todos:
        if node.id == todo.id:
            raise HTTPException(status_code=409, detail="이미 존재하는 ToDo입니다.")
    todos.append(todo)


@router.put("/todos/{id}")
async def update_todo(id):
    pass


@router.delete("/todos/{id}")
async def delete_todo(id: int = Path(..., gt=0)):
    for node in todos:
        if node.id == id:
            todos.remove(node)
            return {"message": "삭제 완료"}
        else:
            raise HTTPException(status_code=404, detail="해당 ToDo가 존재하지 않습니다.")