from pubsub import pub
from . import commands, events, settings
from .repository import repository
from .domain import Order

def place_order(command: commands.PlaceOrder):
    order = Order(command.items)
    repository.insert(order)
    pub.sendMessage(settings.ORDER_CREATED_TOPIC, event=events.OrderCreated(command.id, order.id))

def notify_sales(command: commands.NotifySales):
    print(command.message)

def order_created(event: events.OrderCreated):
    order = repository.get(str(event.order_id))
    message = f"============\nNew Order:\n============\nID: {order.id}\nItems: {order.items}"
    pub.sendMessage(settings.NOTIFY_SALES_TOPIC, command=commands.NotifySales(message))
