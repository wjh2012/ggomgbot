from abc import ABC, abstractmethod


class GPTPort(ABC):
    @abstractmethod
    async def chat(self, message: str) -> str:
        pass
