# 1
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class TaskRead(BaseModel):
#   id: int
#   title: str
#   completed: bool


# tasks_db = [
#   TaskRead(id=1, title="Купить молоко", completed=False),
#   TaskRead(id=2, title="Позвонить другу", completed=True),
#   TaskRead(id=3, title="Сделать домашку", completed=False),
#   TaskRead(id=4, title="Погулять с собакой", completed=True),
#   TaskRead(id=5, title="Записаться на тренировку", completed=False)
# ]


# @app.get('/tasks')
# async def get_tasks() -> list[TaskRead]:
#   return tasks_db




# 2
# from typing import Annotated

# from fastapi import FastAPI, status
# from pydantic import BaseModel, Field

# app = FastAPI()


# class UserBase(BaseModel):
#   """Базовая модель с общими полями"""
#   name: str
#   age: Annotated[int, Field(ge=18)]


# class UserCreate(UserBase):
#   """Модель для создания пользователя (только входные данные)"""
#   pass # Все поля наследуются из UserBase


# class UserRead(UserBase):
#   """Модель для возврата пользователя (с ID)"""
#   id: int


# users_db = []


# @app.post('/users', status_code=status.HTTP_201_CREATED)
# async def create_user(user_create: UserCreate) -> UserRead:
#   new_user = UserRead(id=len(users_db) + 1, name=user_create.name, age=user_create.age)
#   users_db.append(new_user)
#   return new_user




# 3
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel

# app = FastAPI()


# class UserRead(BaseModel):
#   id: int
#   name: str
#   email: str


# users_db = [
#   UserRead(id=1, name="Алексей", email="alexey@example.com"),
#   UserRead(id=2, name="Мария", email="maria@example.com"),
#   UserRead(id=3, name="Иван", email="ivan@example.com"),
#   UserRead(id=4, name="Елена", email="elena@example.com"),
#   UserRead(id=5, name="Дмитрий", email="dmitry@example.com")
# ]


# @app.get("/users/{user_id}")
# async def get_user(user_id: int) -> UserRead:
#   for user in users_db:
#     if user.id == user_id:
#       return user
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")




# 4
# from typing import Annotated

# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel, Field

# app = FastAPI()


# class UserUpdate(BaseModel):
#   name: str
#   age: Annotated[int, Field(gt=0)]


# class UserRead(BaseModel):
#   id: int
#   name: str
#   age: Annotated[int, Field(gt=0)]


# users_db = [
#   UserRead(id=1, name="Алексей", age=25),
#   UserRead(id=2, name="Мария", age=30),
#   UserRead(id=3, name="Иван", age=22),
#   UserRead(id=4, name="Елена", age=28),
#   UserRead(id=5, name="Дмитрий", age=35)
# ]


# @app.put('/users/{user_id}')
# async def update_user(user_id: int, user_update: UserUpdate) -> UserRead:
#   for i, user in enumerate(users_db):
#     if user.id == user_id:
#       updated_user = UserRead(id=user.id, name=user_update.name, age=user_update.age)
#       users_db[i] = updated_user
#       return updated_user
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")




# 5
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel

# app = FastAPI()


# class NoteRead(BaseModel):
#   id: int
#   text: str


# notes = [
#   NoteRead(id=1, text="Купить хлеб"),
#   NoteRead(id=2, text="Написать отчет"),
#   NoteRead(id=3, text="Позвонить маме"),
#   NoteRead(id=4, text="Сходить в спортзал"),
#   NoteRead(id=5, text="Прочитать книгу")
# ]


# @app.delete('/notes/{note_id}')
# async def delete_note(note_id: int) -> NoteRead:
#   for i, note in enumerate(notes):
#     if note.id == note_id:
#       notes.pop(i)
#       return note
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
