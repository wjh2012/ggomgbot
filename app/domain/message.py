import datetime
from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Message:
    sender: Literal["user", "bot"]
    content: str
    timestamp: datetime
