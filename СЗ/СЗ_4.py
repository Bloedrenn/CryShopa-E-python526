# 1
# from typing import Annotated

# from pydantic import BaseModel, EmailStr, Field


# # class UserCreate(BaseModel):
# #   username: str = Field(min_length=3, max_length=50, description="Имя пользователя")
# #   email: EmailStr = Field(description="Электронная почта пользователя")
# #   is_active: bool = Field(default=True, description="Статус активности пользователя")

# class UserCreate(BaseModel):
#   username: Annotated[str, Field(min_length=3, max_length=50, description="Имя пользователя")]
#   email: Annotated[EmailStr, Field(description="Электронная почта пользователя")]
#   is_active: Annotated[bool, Field(description="Статус активности пользователя")] = True




# 2
# from typing import Annotated

# from pydantic import BaseModel, Field


# class TaskCreate(BaseModel):
#   title: Annotated[str, Field(min_length=1, max_length=100, description="Название задачи")]
#   description: Annotated[str | None, Field(max_length=500, description="Описание задачи")] = None
#   is_completed: Annotated[bool, Field(description="Статус завершения задачи")] = False




# 3
# from datetime import datetime
# from decimal import Decimal
# from typing import Annotated

# from pydantic import BaseModel, Field, PositiveInt


# class OrderRead(BaseModel):
#   id: Annotated[PositiveInt, Field(description="Уникальный идентификатор заказа")]
#   user_id: Annotated[PositiveInt, Field(description="Идентификатор пользователя, сделавшего заказ")]
#   total_amount: Annotated[Decimal, Field(description="Общая сумма заказа", ge=0)]
#   created_at: Annotated[datetime, Field(description="Дата и время создания заказа")]




# 4
# from typing import Annotated

# from pydantic import BaseModel, Field, PositiveInt


# class AddressRead(BaseModel):
#   user_id: Annotated[PositiveInt, Field(description="Идентификатор пользователя")]
#   city: Annotated[str, Field(min_length=2, max_length=100, description="Город")]
#   street: Annotated[str, Field(min_length=2, max_length=200, description="Улица")]
#   postal_code: Annotated[int, Field(ge=101000, le=999999, description="Почтовый индекс")]




# 5
# from datetime import datetime, UTC
# from typing import Annotated

# from pydantic import BaseModel, Field, SecretStr, EmailStr


# class UserCreate(BaseModel):
#   username: Annotated[str, Field(min_length=5, max_length=20, description="Пользовательское имя, от 5 до 20 символов")]
#   password: Annotated[SecretStr, Field(min_length=8, max_length=50, description="Пароль, от 8 до 50 символов")]
#   email: Annotated[EmailStr, Field(description="Электронная почта")]
#   first_name: Annotated[str | None, Field(min_length=2, max_length=30, description="Имя, от 2 до 30 символов")] = None
#   last_name: Annotated[str | None, Field(min_length=2, max_length=30, description="Фамилия, от 2 до 30 символов")] = None
#   is_active: Annotated[bool, Field(description="Учётная запись активна")] = True
#   is_staff: Annotated[bool, Field(description="Является служебным пользователем")] = False
#   is_superuser: Annotated[bool, Field(description="Является суперпользователем")] = False
#   date_joined: Annotated[datetime, Field(default_factory=lambda: datetime.now(UTC), description="Зарегистрирован")]
#   last_login: Annotated[datetime | None, Field(description="Последнее посещение")] = None


# # Создание объекта с минимальными данными (только обязательные поля)
# minimal_user = UserCreate(
#   username="testuser",
#   password="TestPass123",
#   email="test@example.com"
# )

# print(f"Дата регистрации: {minimal_user.date_joined}\n")
# print(f"Пароль (замаскированный): {minimal_user.password}")
# print(f"Пароль (расшифрованный): {minimal_user.password.get_secret_value()}")
