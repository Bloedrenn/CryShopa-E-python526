from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

users_db = {
  1: {"name": "Joshua", "age": 22},
  2: {"name": "Max", "age": 35}
}


# Создаём модель (схему), наследующуюся от BaseModel
class UserGet(BaseModel):
  # Определяем поля модели и их типы.
  name: str
  age: int


@app.get("/users/{user_id}") # Можно написать здесь: response_model=UserGet
async def get_user(
  user_id: int
) -> UserGet:
  try:
    return users_db[user_id]
  except:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )
