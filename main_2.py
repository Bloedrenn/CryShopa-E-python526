from typing import Annotated

from fastapi import Body, FastAPI, HTTPException, Path, status

app = FastAPI()

PathID = Annotated[int, Path(ge=1)]


def is_user_in_db(user_id: int) -> bool:
  if user_id not in users_db:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  
  return True


def get_user_from_db(user_id: int) -> dict:
  if is_user_in_db(user_id):
    return users_db[user_id]


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
  user_id: PathID
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


@app.put("/users/{user_id}")
async def update_user(
  user_id: PathID,
  name: Annotated[str, Body(max_length=30)],
  age: Annotated[int, Body(ge=1, le=120)]
) -> dict:
  is_user_in_db(user_id)

  updated_user = {
    "name": name,
    "age": age
  }
  users_db[user_id] = updated_user
  # return "User updated!"
  return updated_user


@app.patch("/users/{user_id}")
async def patch_user(
  user_id: PathID,
  name: Annotated[str | None, Body(max_length=30)] = None,
  age: Annotated[int | None, Body(ge=1, le=120)] = None
) -> dict:
  user = get_user_from_db(user_id)

  if name is None and age is None:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="You must update at least one field"
    )

  if name is not None:
    user['name'] = name
  if age is not None:
    user['age'] = age

  return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: PathID) -> str:
  is_user_in_db(user_id)
  users_db.pop(user_id)
  return f"User ID={user_id} was deleted!"


@app.delete("/users", status_code=status.HTTP_204_NO_CONTENT)
async def delete_users():
  users_db.clear()
# Ещё вариант:
# @app.delete("/users")
# async def delete_users() -> str:
#   users_db.clear()
#   return "All users were deleted!"
