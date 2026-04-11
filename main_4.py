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




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, Field


# class ArticleCreate(BaseModel):
#   text: str
#   slug: Annotated[str, Field(pattern=r'^[-a-zA-Z0-9_]+$')]


# # Примеры использования:
# valid_article = ArticleCreate(text="Some text 1", slug="valid-slug_123")
# # invalid_article_1 = ArticleCreate(text="Some text 2", slug="Invalid Slug!") # Ошибка
# # invalid_article_2 = ArticleCreate(text="Some text 3", slug="") # Ошибка




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, Field, field_validator


# class MessageCreate(BaseModel):
#   content: Annotated[str, Field(min_length=1, max_length=500)]

#   @field_validator("content")
#   @classmethod
#   def check_forbidden_words(cls, value):
#     forbidden_words = ["spam", "offensive"]
#     if any(forbidden_word in value.lower() for forbidden_word in forbidden_words):
#       raise ValueError("Message contains forbidden words")
#     return value


# message = MessageCreate(content="Hello, world!") # OK
# # message = Message(content="This is spam") # Ошибка: Message contains forbidden words




# ========================================================================================= #
# from pydantic import BaseModel, field_validator


# class MessageRead(BaseModel):
#   id: int
#   content: str

#   @field_validator("content")
#   @classmethod
#   def check_content_id_match(cls, value, info):
#     # Параметр info в @field_validator предоставляет доступ к полям модели через info.data
#     # print(info.data)
#     if str(info.data['id']) not in value:
#       raise ValueError("Content must contain the ID")
#     return value


# message = MessageRead(id=1, content="Hello, Misha (1)") # OK
# # message = MessageRead(id=4, content="Hello, Tom (5)") # Ошибка: Content must contain the ID
# # message = MessageRead(id=7, content="How are you?") # Ошибка: Content must contain the ID




# ========================================================================================= #
# from pydantic import BaseModel, EmailStr, model_validator


# class UserCreate(BaseModel):
#   name: str
#   age: int
#   email: EmailStr | None = None

#   @model_validator(mode='after')
#   # mode='after': валидация после преобразования данных в типы модели (чаще используется)
#   def check_age_and_email(self):
#     if self.age < 18 and self.email:
#       raise ValueError("Несовершеннолетним нельзя указывать email")
#     return self


# # message = UserCreate(name="Misha", email="example@mail.ru", age=21) # OK
# # message = UserCreate(name="Misha", age=13) # OK
# # message = UserCreate(name="Misha", email="example@mail.ru", age=15) # Ошибка: Несовершеннолетним нельзя указывать email


# # Пример валидации без объекта модели:
# # data = {"name": "Alice", "age": 22, "email": "alice@example.com"}
# data = {"name": "Alice", "age": 16, "email": "alice@example.com"}
# try:
#   UserCreate.model_validate(data)
# except ValueError as e:
#   print(e)




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, StringConstraints

# Username = Annotated[str, StringConstraints(min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")]


# class UserCreate(BaseModel):
#   username: Username


# # user = UserCreate(username="john_doe") # OK
# user = UserCreate(username="ab") # Ошибка




# ========================================================================================= #
# from decimal import Decimal
# from typing import Annotated

# from pydantic import BaseModel, Field


# class ProductCreate(BaseModel):
#   price: Annotated[Decimal, Field(max_digits=6, decimal_places=2)] # Например, 1234.56


# # product = ProductCreate(price=109.90) # OK
# product = ProductCreate(price=1234567.89) # Ошибка: слишком много цифр




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, Field


# class Message(BaseModel):
#   id: Annotated[int, Field(strict=True)]
#   # strict=True: запрещает преобразование типов для поля


# message = Message(id=123) # OK
# # message = Message(id="123") # Ошибка: String is not allowed in strict mode




# ========================================================================================= #
# from typing import Annotated

# from pydantic import BaseModel, Field


# class OrderRead(BaseModel):
#   id: Annotated[int, Field(ge=1)]
#   # Модель ожидает только поле id типа int.


# OrderRead(id=5, age=22) # НО, ошибки нет!
# # По умолчанию Pydantic игнорирует лишние поля (т. е. можно случайно лишнее передать).
