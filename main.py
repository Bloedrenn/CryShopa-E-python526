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
