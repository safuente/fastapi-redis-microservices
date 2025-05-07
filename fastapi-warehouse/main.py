from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from models import Product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.post('/product', tags=['warehouse'])
def create_product(product: Product):
    return product.save()


@app.get('/product/{pk}', tags=['warehouse'])
def get_product(pk: str):
    return Product.get(pk)


@app.get('/products', tags=['warehouse'])
def get_all_products():
    return [Product.get(pk) for pk in Product.all_pks()]


@app.delete('/product/{pk}', tags=['warehouse'])
def delete(pk: str):
    return Product.delete(pk)
