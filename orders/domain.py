
from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Order:
    items: List[str]
    id: UUID = field(default_factory=uuid4)
