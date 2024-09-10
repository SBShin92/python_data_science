from pydantic import BaseModel, Field

todos = []

class Todo(BaseModel):
    id: int = Field(None, json_schema_extra={
      "example": "1"
    })
    title: str|None = Field(..., json_schema_extra={
      "example": "저녁 재료 구매하러 마트 방문"
    })
    done: bool = Field(False, description="할 일 완료 여부")
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "집에 가다가 마트에서 재료 사기",
                "done": False
            }
        }
    }