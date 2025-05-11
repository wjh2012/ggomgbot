from app.application.ports.inbound.receive_message_port import ReceiveMessagePort
from app.application.ports.outbound.send_message_port import SendMessagePort


class ChatService(ReceiveMessagePort):
    def __init__(self, send_message_port: SendMessagePort):
        self.send_message_port = send_message_port

    async def on_message(self, user_id: str, message: str, channel_id: str) -> str:
        if message.startswith("콩쥐"):
            response = await self.send_message_port.send_message(message)
            return response
        return ""
