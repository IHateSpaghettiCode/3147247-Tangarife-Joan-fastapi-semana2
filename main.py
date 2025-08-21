from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="My fastapi en semana 2")

# Modelos de datos
class Product(BaseModel):
    name: str
    price: int
    available: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    available: bool
    message: str = "Successful operation"

class ProductListResponse(BaseModel):
    products: List[dict]
    total: int
    message: str = "List retrieved"

# Almacenamiento temporal
products = []

# Endpoints básicos
@app.get("/")
def hello_world() -> dict:
    return {"message": "la semana 2 con fastapi con Pydantic y Type Hints!"}

@app.get("/products", response_model=ProductListResponse)
def get_products() -> ProductListResponse:
    return ProductListResponse(
        products=products,
        total=len(products)
    )

@app.post("/products", response_model=ProductResponse)
def create_product(product: Product) -> ProductResponse:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)

    return ProductResponse(**product_dict, message="Product created")

@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/search")
def search_products(
    name: Optional[str] = None,
    max_price: Optional[int] = None
) -> dict:
    results = products.copy()

    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]

    return {"results": results, "total": len(results)}



#from fastapi import FastAPI

#app = FastAPI(title="My First API")

# Endpoint 1: Hello World
#@app.get("/")
#def hello_world() -> dict:
#    return {"message": "My first FastAPI!"}

# Endpoint 2: Greeting con parámetro
#@app.get("/greeting/{name}")
#def greet_user(name: str) -> dict:
#    return {"greeting": f"Hello {name}!"}

# Endpoint 3: Cálculo con múltiples parámetros
#@app.get("/calculate/{num1}/{num2}")
#def calculate(num1: int, num2: int) -> dict:
#    result = num1 + num2
#    return {"result": result, "operation": "sum"}

# Endpoint 4: Info básica
#@app.get("/info")
#def info() -> dict:
#    return {"api": "FastAPI", "week": 2, "status": "running"}

# Endpoint 5: Mi perfil
#@app.get("/my-profile")
#def my_profile() -> dict:
#    return {
#        "name": "Joan",
#        "bootcamp": "FastAPI",
#        "week": 2,
#        "date": "2025",
#        "likes_fastapi": True
#    }
