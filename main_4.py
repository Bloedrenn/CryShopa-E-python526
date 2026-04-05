# from pydantic import BaseModel


# class MessageRead(BaseModel):
#   id: int
#   content: str
#   tags: list[str] | None = None # Необязательное поле, по умолчанию None.
#   priority: int = 0 # Необязательное поле, по умолчанию 0.


# Пример использования
# message = MessageRead(id=1, content="Hello, Pydantic!", tags=["important", 'new']) # Создает экземпляр модели, автоматически валидируя данные.
# print(message) # Вывод: id=1 content='Hello, Pydantic!'
# print(message.id)
# print(message.content)


# print(message.model_dump()) # Преобразование в словарь: {'id': 1, 'content': 'Hello, Pydantic!'}
# print(message) # Всё ещё объект
# Этот метод преобразует объект Pydantic в Python-словарь (dict).
# Он полезен, когда нужно получить данные модели в виде словаря для дальнейшей обработки в коде.


# print(message.model_dump_json()) # Преобразование в JSON-строку: '{"id": 1, "content": "Hello, Pydantic!"}'
# Этот метод сериализует объект Pydantic в JSON-строку.
# Он полезен, когда нужно получить данные в формате JSON для отправки по сети или сохранения.


# message = Message(id="not_an_integer", content="Hello") # Pydantic выдаст ошибку валидации




# ========================================================================================= #
# from pydantic import BaseModel, EmailStr, HttpUrl, PositiveInt


# class UserCreate(BaseModel):
#   email: EmailStr
#   website: HttpUrl
#   age: PositiveInt


# user = UserCreate(email='example@mail.com', website='https://github.com/', age=18)




# ========================================================================================= #
# from pydantic import BaseModel, EmailStr


# class AuthorRead(BaseModel):
#   id: int
#   name: str
#   email: EmailStr


# class MessageRead(BaseModel):
#   id: int
#   content: str
#   author: AuthorRead # Вложенная модель


# message = MessageRead(
#   id=5,
#   content="Hello bratha",
#   author=AuthorRead(id=3, name="Alice", email="alice@example.com")
# )
# print(message.model_dump_json())




# ========================================================================================= #
# from pydantic import BaseModel, StrictInt


# class MessageRead(BaseModel):
#   id: StrictInt
#   content: str
#   metadata: dict[str, int] # Словарь с ключами-строками и значениями-числами


# message = MessageRead(
#   id="123", # Строку "123" Pydantic преобразует в int
#   content="Hello, Pydantic!",
#   metadata={
#     "charset": 8,
#     "code": 11
#   }
# )

# print(message) # Вывод: id=123 content='Hello'




# ========================================================================================= #
# from pydantic import BaseModel, SecretStr


# class UserCreate(BaseModel):
#   username: str
#   password: SecretStr


# user = UserCreate(
#   username="alice",
#   password="gladiator5000"
# )

# print(user) # Получим: username='alice' password=SecretStr('**********')
# print(user.password)

# # Чтобы получить реальное значение пароля:
# # print(
# #   user.password.get_secret_value()
# # )




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, Field


# class MessageRead(BaseModel):
#   id: Annotated[int, Field(gt=0)] # Число: больше 0
#   content: Annotated[str, Field(min_length=1, max_length=500, pattern=r"^[a-zA-Z0-9\s!,.?]*$")] # Строка: 1-500 символов, только буквы, цифры, пробельные символы и конкретные знаки
#   priority: Annotated[
#     float,
#     Field(ge=0.0, le=10.0)
#   ] = 0.0 # Число: необязательное, от 0 до 10


# message = MessageRead(id=1, content="Hello, world!", priority=5.0)
# print(message)
