from dataclasses import dataclass
from typing import List
from .message import Message

@dataclass(frozen=True)
class Command(Message):
    ...

@dataclass(frozen=True)
class PlaceOrder(Command):
    items: List[str]

@dataclass(frozen=True)
class NotifySales(Command):
    message: str
