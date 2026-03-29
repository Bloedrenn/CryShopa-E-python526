from fastapi import FastAPI

app = FastAPI()

# Это словарь, имитирующий базу данных. Ключи — целые числа (ID пользователей), значения — словари (данные пользователей).
users_db = {
  1: {"name": "Joshua", "age": 22},
  2: {"name": "Max", "age": 35}
}


@app.get("/users")
async def get_users() -> dict:
  return users_db
