from abc import ABC, abstractmethod


class ChatUseCase(ABC):
    @abstractmethod
    async def ask(self, user_id: str, message: str, channel_id: str) -> str:
        pass
