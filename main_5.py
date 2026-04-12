from typing import Annotated

from fastapi import FastAPI, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates") # Настройка Jinja2
app.mount("/static", StaticFiles(directory="static"))


class MessageRead(BaseModel):
  id: int
  content: str


messages_db: list[MessageRead] = [
  MessageRead(id=1, content="Hello Dmitriy"),
  MessageRead(id=2, content="How are you Max?"),
]


# Страница всех сообщений
@app.get("/web/messages") # Можно так: response_class=HTMLResponse
async def get_messages_page(request: Request) -> HTMLResponse:
  return templates.TemplateResponse("index.html", {"request": request, "messages": messages_db})


# Страница создания сообщения
@app.get("/web/messages/create", name="create_message_page")
async def get_create_message_page(request: Request) -> HTMLResponse:
  return templates.TemplateResponse("create.html", {"request": request})


# Обработка формы создания сообщения
@app.post("/web/messages")
async def handle_create_message_form(
  content: Annotated[str, Form()]
) -> HTMLResponse:
  next_id = max((msg.id for msg in messages_db), default=0) + 1
  new_message = MessageRead(id=next_id, content=content)
  messages_db.append(new_message)
  return RedirectResponse(url="/web/messages", status_code=status.HTTP_303_SEE_OTHER)


# Страница одного сообщения
@app.get("/web/messages/{message_id}")
async def get_message_detail_page(request: Request, message_id: int) -> HTMLResponse:
  for message in messages_db:
    if message.id == message_id:
      return templates.TemplateResponse("detail.html", {"request": request, "message": message})
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Сообщение не найдено")
