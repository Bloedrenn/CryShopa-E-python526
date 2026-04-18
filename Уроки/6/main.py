from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Messages CRUD")

# Настраиваем CORS для взаимодействия с фронтендом
app.add_middleware(
  CORSMiddleware,
  allow_origins=["null"], # allow_origins=["*"] - если надо разрешить запросы со всех источников
  allow_methods=["*"],
)


# Модель Pydantic для создания нового сообщения
class MessageCreate(BaseModel):
  content: str


# Модель Pydantic для полного обновления сообщения
class MessageUpdate(MessageCreate):
  pass


# Модель Pydantic для частичного обновления сообщения (для PATCH-запросов)
class MessagePatch(BaseModel):
  content: str | None = None


# Модель Pydantic для представления сообщения в ответах API
class Message(BaseModel):
  id: int
  content: str


# Простая "база данных" в памяти для хранения сообщений
messages_db: list[Message] = [
  Message(id=1, content="Привет Миша"),
  Message(id=2, content="Как дела, Маша?"),
]


# Вспомогательная функция для генерации следующего ID
def next_id() -> int:
  return max((m.id for m in messages_db), default=0) + 1


# Вспомогательная функция для получения индекса сообщения из списка (БД) по ID
def get_index(message_id: int) -> int:
  for i, m in enumerate(messages_db):
    if m.id == message_id:
      return i
  return -1


# Эндпоинт для получения списка сообщений
@app.get("/messages")
async def get_messages() -> list[Message]:
  return messages_db


# Эндпоинт для получения одного сообщения
@app.get("/messages/{message_id}")
async def get_message(message_id: int) -> Message:
  idx = get_index(message_id)
  if idx < 0:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
  return messages_db[idx]


# Эндпоинт для создания сообщения
@app.post("/messages", status_code=status.HTTP_201_CREATED)
async def create_message(payload: MessageCreate) -> Message:
  m = Message(id=next_id(), content=payload.content)
  messages_db.append(m)
  return m


# Эндпоинт для полного обновления сообщения
@app.put("/messages/{message_id}")
async def full_update_message(message_id: int, payload: MessageUpdate) -> Message:
  idx = get_index(message_id)
  if idx < 0:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
  updated = Message(id=message_id, content=payload.content)
  messages_db[idx] = updated
  return updated
  # Почему мы создаем новый объект, а не изменяем существующий?
  # Когда у нас создаётся новый объект Message с помощью конструктора Message(id=message_id, content=payload.content), то Pydantic автоматически валидирует входные данные (id и content) в соответствии с правилами, заданными в модели Message.
  # В случае, если мы берем уже существующий объект Message, который был создан ранее, и просто изменяем поле content, присваивая значение из payload.content напрямую, то Pydantic не участвует в этом процессе, так как вы не создаёте новый объект Message и не вызываете конструктор модели.
  # Pydantic проводит валидацию только при создании нового экземпляра модели (по умолч.) или при использовании методов, явно вызывающих валидацию. В результате значение payload.content присвоится без проверки на соответствие валидационным правилам, определённым в модели Message. И этот подход позволит сохранить в messages_db данные, которые могут привести к ошибкам в дальнейшем (например, при сериализации или обработке данных).


# Эндпоинт для частичного обновления сообщения
@app.patch("/messages/{message_id}")
async def partial_update_message(message_id: int, payload: MessagePatch) -> Message:
  # Ищем индекс сообщения по ID
  idx = get_index(message_id)
  
  # Если сообщение не найдено, возвращаем ошибку 404
  if idx < 0:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
  
  # Обновляем только переданные поля
  if payload.content is not None:
    messages_db[idx].content = payload.content
  
  return messages_db[idx]


# Эндпоинт для удаления сообщения
@app.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(message_id: int):
  # Ищем индекс сообщения по ID
  idx = get_index(message_id)
  
  # Если сообщение не найдено, возвращаем ошибку 404
  if idx < 0:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
  
  # Удаляем сообщение из базы данных
  messages_db.pop(idx)
