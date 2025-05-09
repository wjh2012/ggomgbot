from app.core.port.inbound.chat_use_case import ChatUseCase
from app.core.port.outbound.gpt_port import GPTPort


class ChatService(ChatUseCase):
    def __init__(self, gpt: GPTPort):
        self.gpt = gpt

    async def ask(self, user_id: str, message: str, channel_id: str) -> str:
        response = await self.gpt.chat(message)
        return response
