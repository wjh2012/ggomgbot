from app.core.port.outbound.bot_port import BotPort


class BotService:
    def __init__(self, bot_port: BotPort):
        self.bot_port = bot_port

    async def rename_bot(self, guild_id: int, new_name: str):
        await self.bot_port.change_nickname(guild_id, new_name)
