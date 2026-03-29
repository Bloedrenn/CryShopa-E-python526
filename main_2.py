from typing import Annotated

from fastapi import Body, FastAPI, HTTPException, Path, status

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


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
  name: Annotated[str, Body(max_length=30)],
  age: Annotated[int, Body(ge=1, le=120)]
) -> dict: # Теперь здесь тело запроса
  new_index = max(users_db) + 1 if users_db else 1
  new_user = {"name": name, "age": age}
  users_db[new_index] = new_user
  # return "User created!"
  return new_user
