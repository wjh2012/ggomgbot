from abc import ABC, abstractmethod


class SendMessagePort(ABC):
    @abstractmethod
    async def send_message(self, message: str) -> str:
        pass
