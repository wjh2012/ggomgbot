from app.config.env_config import get_settings

config = get_settings()


class OpenAiClient:
    def __init__(self, client):
        self.client = client

    async def chat(self):
        response = await self.client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "친절한 도우미입니다."},
                {"role": "user", "content": "안녕 GPT야!"},
            ],
        )
        print(response.choices[0].message.content)
