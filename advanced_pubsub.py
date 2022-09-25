from pubsub import pub
from orders import commands, handlers, settings

pub.subscribe(handlers.place_order, settings.PLACE_ORDER_TOPIC)
pub.subscribe(handlers.order_created, settings.ORDER_CREATED_TOPIC)
pub.subscribe(handlers.notify_sales, settings.NOTIFY_SALES_TOPIC)

pub.sendMessage(settings.PLACE_ORDER_TOPIC, command=commands.PlaceOrder(items=["100 inch TV", "magic carpet"]))
pub.sendMessage(settings.PLACE_ORDER_TOPIC, command=commands.PlaceOrder(items=["soft cheese", "dutch mashrooms"]))
