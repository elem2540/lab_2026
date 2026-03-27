from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")


products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 5.99},
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        context={
            "request": request,
            "text": "Welcome to the store!"
        }
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    return templates.TemplateResponse(
        name="products.html",
        context={
            "request": request,
            "products": products
        }
    )
