from app.config.env_config import get_settings
from app.core.port.outbound.gpt_port import GPTPort

config = get_settings()


class OpenAiClient(GPTPort):
    def __init__(self, client):
        self.client = client

    async def chat(self, message: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "친한 친구. 격식없는 대화."},
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content
