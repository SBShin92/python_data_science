from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="인사", description="인사 메시지")
def read_root():
    return {"Hello": "World"}

@app.get("/hidden-endpoint", include_in_schema=False)  # 제외 엔드포인트
def hidden_endpoint():
    return {"message": "이 엔드포인트는 스웨거 문서에 표시되지 않습니다."}


@app.get("/items/{item_id}", summary="아이템 조회", description="아이템 정보")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    아이템 조회 API
    @param item_id: 아이템 ID
    @param q: 쿼리스트링
    """
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    