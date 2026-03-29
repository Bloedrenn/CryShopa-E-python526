from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, status

app = FastAPI()

# Это словарь, имитирующий базу данных. Ключи — целые числа (ID пользователей), значения — словари (данные пользователей).
users_db = {
  1: {"name": "Joshua", "age": 22},
  2: {"name": "Max", "age": 35}
}


@app.get("/users")
async def get_users() -> dict:
  return users_db


@app.get("/users/{user_id}")
async def get_user(
  user_id: Annotated[int, Path(ge=1)]
) -> dict:
  try:
    return users_db[user_id]
  except:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )


  # Вариант с .get():
  # user = users_db.get(user_id)

  # if user is None:
  #   raise HTTPException(
  #     status_code=status.HTTP_404_NOT_FOUND,
  #     detail="User not found"
  #   )
  
  # return user
