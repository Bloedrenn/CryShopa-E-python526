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
