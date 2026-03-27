from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel


class Product(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3)]


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")


products_list = [
    {"name": "Product 1", "price": 10.99, "location": "Shelf A"},
    {"name": "Product 2", "price": 19.99, "location": "Shelf B"},
    {"name": "Product 3", "price": 5.99,  "location": "Shelf C"},
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # home.html si aspetta `text.title` e `text.message`
    return templates.TemplateResponse(
        name="home.html",
        context={
            "request": request,
            "text": {"title": "Benvenuto", "message": "Benvenuto nel nostro negozio!"}
        }
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    # il template products.html si aspetta una variabile `product_list`
    return templates.TemplateResponse(
        name="products.html",
        context={
            "request": request,
            "product_list": products_list
        }
    )


@app.get("/product_form", response_class=HTMLResponse)
def add_product(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="product_form.html"
    )


@app.post("/insert_product")
def insert_product(
    name: Annotated[str, Form(), Field(min_length=3, max_length=30)],
    price: Annotated[float, Form(), Field(gt=0)],
    location: Annotated[str, Form(), Field(min_length=3)]
):
    product = {"name": name, "price": price, "location": location}
    return "Product added successfully!"


@app.post("/insert_product_json")
def insert_product_json(
    product: Product
):
    print(product)