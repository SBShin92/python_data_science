from fastapi import APIRouter, Query
from typing import List, Optional

router = APIRouter(tags=["params"])


@router.get("/items", description="단일 쿼리 파람")
async def read_items(q: str):
    return {"message": f"{q}"}


@router.get("/users", description="여러개의 쿼리 파람")
async def read_users(age: int, name: Optional[str] = None):
    return {"name": name, "age": age}


@router.get("/items/multi", description="리스트 받기")
async def read_items_multi(q: Optional[List[str]] = Query(None)):
    return {"message": q}


@router.get("/search")
async def search_item(keyword: str = Query(min_length=3)):
    return {"message": keyword}