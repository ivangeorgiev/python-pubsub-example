from dataclasses import dataclass
from uuid import UUID
from .message import Message

@dataclass(frozen=True)
class Event(Message):
    ...

@dataclass(frozen=True)
class OrderCreated(Event):
    command_id: UUID
    order_id: str
