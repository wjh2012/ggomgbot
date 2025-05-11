from abc import ABC, abstractmethod


class ReceiveMessagePort(ABC):
    @abstractmethod
    async def on_message(self, user_id: str, message: str, channel_id: str) -> str:
        pass
