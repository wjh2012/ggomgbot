from app.application.ports.outbound.nickname_port import NickNamePort


class DiscordBotAdapter(NickNamePort):
    def __init__(self):
        self.bot = None

    def set_bot(self, bot_instance):
        self.bot = bot_instance

    async def change_nickname(self, guild_id: int, new_name: str):
        if not self.bot:
            raise ValueError("Bot instance not set in DiscordBotController")

        guild = self.bot.get_guild(guild_id)
        if guild:
            me = guild.me
            await me.edit(nick=new_name)
