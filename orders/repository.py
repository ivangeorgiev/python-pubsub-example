from dataclasses import asdict
from uuid import UUID
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from .domain import Order

class OrderRepository:
    def __init__(self):
        self._db = TinyDB(storage=MemoryStorage)

    @property
    def db(self):
        return self._db

    def insert(self, order: Order):
        stored_order = asdict(order)
        stored_order["id"] = str(order.id)
        self.db.insert(stored_order)

    def get(self, order_id: str):
        stored_order = self.db.get(Query().id == order_id)
        if stored_order:
            return Order(stored_order["items"], UUID(stored_order["id"]))
        raise KeyError(f"Order '{order_id}' was not found")

repository = OrderRepository()
