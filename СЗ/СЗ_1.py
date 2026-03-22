from fastapi import FastAPI

app = FastAPI()


# 1
@app.get('/products/{product_id}')
async def detail_view(product_id: int) -> dict:
    return {"product": f"Stock number {product_id}"}


# 2
@app.get("/users/{name}/{age}")
async def user(name: str, age: int) -> dict:
    return {"user_name": name, "user_age": age}


# 3
# Порядок верный?
@app.get("/users/admin")
async def admin() -> dict:
    return {"message": "Hello admin"}


@app.get("/users/{name}")
async def get_user(name: str) -> dict:
    return {"user_name": name}


# 4
@app.get("/product")
async def get_product_detail(item_id: int) -> dict:
    return {"product": f"Stock number {item_id}"}


# 5
@app.get("/users")
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {"user_name": name, "user_age": age}


# 6
country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}


@app.get("/country/{country}")
async def list_cities(country: str, limit: int | None = None) -> dict:
    cities = country_dict.get(country)
    return {
        "country": country,
        "cities": cities[:limit] if cities is not None else None
    }
