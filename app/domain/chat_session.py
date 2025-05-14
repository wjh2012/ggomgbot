from dataclasses import dataclass, field

from app.domain.message import Message
from app.domain.user import User


@dataclass
class ChatSession:
    session_id: str
    user: User
    history: list[Message] = field(default_factory=list)

    def add_message(self, message: Message) -> None:
        self.history.append(message)
        if message.sender == "user":
            self.user.update_last_active()
