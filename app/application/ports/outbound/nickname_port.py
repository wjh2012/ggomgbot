from abc import ABC, abstractmethod


class NickNamePort(ABC):
    @abstractmethod
    async def change_nickname(self, guild_id: int, new_name: str):
        pass
