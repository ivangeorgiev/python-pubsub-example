from typing import Dict, List
from uuid import UUID, uuid4
from pubsub import pub

PLACE_ORDER_TOPIC = 'place-order'
ORDER_CREATED_TOPIC = 'order-created'

orders: Dict[UUID, dict] = {}

def place_order(items: List[str]):
    order = { "id": uuid4(), "items": items.copy()}
    orders[order["id"]] = order
    pub.sendMessage(ORDER_CREATED_TOPIC, order_id=order["id"])

def notify_sales(message: str):
    print(message)

def order_created(order_id: UUID):
    order = orders[order_id]
    notify_sales(f"============\nNew Order:\n============\nID: {order['id']}\nItems: {order['items']}")

pub.subscribe(place_order, PLACE_ORDER_TOPIC)
pub.subscribe(order_created, ORDER_CREATED_TOPIC)

pub.sendMessage(PLACE_ORDER_TOPIC, items=["100 inch TV", "magic carpet"])
pub.sendMessage(PLACE_ORDER_TOPIC, items=["soft cheese", "dutch mashrooms"])
