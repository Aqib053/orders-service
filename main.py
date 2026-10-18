from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Order(BaseModel):
    id: int
    customer_name: str
    total: float


@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    return Order(id=order_id, customer_name="Asha", total=499.0)
