from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

from models import ProductOrder, Order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.post('/orders')
def create_product_order(product_order: ProductOrder):
    req = requests.get(f'http://localhost:8000/product/{product_order.product_id}')
    product = req.json()
    fee = product.get('price') * 0.2
    order = Order(
        product_id=product_order.product_id,
        price=product.get('price'),
        fee=fee,
        total=product.get('price') + fee,
        quantity=product_order.quantity,
        status='pending'
    )
    return order.save()


@app.get('/orders/{pk}', tags=['store'])
def get_order(pk: str):
    return Order.get(pk)


@app.get('/orders', tags=['store'])
def get_all_orders():
    return [Order.get(pk) for pk in Order.all_pks()]


