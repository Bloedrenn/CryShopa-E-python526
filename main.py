from fastapi import FastAPI, Path

app = FastAPI(
    title="Первый проект на FastAPI",
    description="Ультра **мега** проект на который потрачено 9 жизней",
    # docs_url=None,
    # redoc_url=None
)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"msg": f'Hello {first_name} {last_name}'}


@app.get("/order/{order_id}")
async def get_order(order_id: int) -> dict:
    return {"id": order_id}


# Все фиксированные пути должны быть объявлены первыми перед динамических путями с параметрами пути
@app.get("/user/profile")
async def profile() -> dict:
    return {"profile": "View profile user"}


@app.get("/user/{user_name}")
async def user(user_name: str) -> dict:
    return {"user": user_name}


@app.get("/user")
async def login(age: int, username: str | None = None) -> dict: # Можно так: "username: Optional[str] = None", но много лишнего кода (нужен импорт)
    # if username == "гость":
    #     return {"age": age}
    if username is None:
        return {"age": age}

    return {"user": username, "age": age}


# Несмотря на то, что параметры пути предшествуют параметрам запроса в URL-адресе, нет необходимости следовать порядку при их объявлении в определении функции
@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}


@app.get("/user/{username}/{age}")
async def login_user(
    username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Ilya'),
    age: int = Path(ge=0, le=100, description="Enter your age")
) -> dict:
    return {"user": username, "age": age}
