from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


# 1
@app.get("/user_name")
async def greet(
  first_name: Annotated[
    str | None, Query(max_length=10, pattern="^J|s$")
  ] = None
) -> dict:
  return {"name": first_name}


# 2
@app.get("/category/{category_id}/products")
async def category(
  category_id: Annotated[int, Path(gt=0, description="Category ID")],
  page: int
) -> dict:
  return {'category_id': category_id, 'page': page}


# 3
profiles_dict = {
  'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
  'dima': {'name': 'Дима', 'age': 40, 'phone': '+79221345212', 'email': 'dima@my-site.com'},
}


@app.get("/users/profiles")
async def retrieve_user_profile(
  username: Annotated[str, Query(min_length=2, max_length=20, description='Имя пользователя')]
) -> dict:
  return profiles_dict.get(username, {'message': f'Пользователь {username} не найден.'})
