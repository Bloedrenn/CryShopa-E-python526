from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

users_db = {
  1: {"name": "Joshua", "age": 22, "password": "sha256lfgkr&fkrejqw2325werw2325werw"},
  2: {"name": "Max", "age": 35, "password": "sha256eqweq2312325werw2eqwe112edqwe"}
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


@app.get("/users")
async def get_users() -> list[UserGet]:
  users = [user for user in users_db.values()]
  return users


class UserCreate(BaseModel): # Можно использовать и для PUT
  name: str
  age: int
  password: str


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate) -> UserGet: # UserCreate - аналог body
  # print(user_create)
  # print(user_create.name)
  # print(user_create.model_dump())

  new_index = max(users_db) + 1 if users_db else 1
  new_user = user_create.model_dump()
  users_db[new_index] = new_user
  return new_user


class UserFullUpdate(BaseModel):
  name: str
  age: int
  password: str


@app.put("/users/{user_id}")
async def update_user(
  user_id: int,
  user_full_update: UserFullUpdate
) -> UserGet:
  if user_id not in users_db:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

  # Имитация шифрования пароли
  user_full_update.password = f'sha256lfgdklkkdh_ewq2{user_full_update.password}'

  updated_user = user_full_update.model_dump()
  users_db[user_id] = updated_user
  return updated_user
