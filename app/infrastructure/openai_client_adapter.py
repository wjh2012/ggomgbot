from app.application.ports.outbound.send_message_port import SendMessagePort
from app.config.env_config import get_settings

config = get_settings()


class OpenAiClientAdapter(SendMessagePort):
    def __init__(self, client):
        self.client = client

    async def send_message(self, message: str) -> str:
        response = await self.client.send_message.completions.create(
            model="o3-mini",
            messages=[
                {
                    "role": "system",
                    "content": "격식없는 대화. 너의 이름은 콩쥐",
                },
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content
