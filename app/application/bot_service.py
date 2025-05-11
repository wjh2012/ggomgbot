from app.application.ports.outbound.nickname_port import NickNamePort


class BotService:
    def __init__(self, nick_name_port: NickNamePort):
        self.nick_name_port = nick_name_port

    async def rename_bot(self, guild_id: int, new_name: str):
        await self.nick_name_port.change_nickname(guild_id, new_name)
