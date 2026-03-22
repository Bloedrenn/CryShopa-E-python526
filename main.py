from fastapi import FastAPI

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
