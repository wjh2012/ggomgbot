from discord.ext import commands


class DiscordBotAdapter(commands.Bot):
    def __init__(self, chat_service, bot_service, **kwargs):
        super().__init__(**kwargs)
        self.chat_service = chat_service  # DI 주입
        self.bot_service = bot_service

    async def setup_hook(self):
        await self.load_extension("app.adapters.inbound.cogs.gptCog")
        await self.load_extension("app.adapter.inbound.cogs.adminCog")

    async def on_ready(self):
        print(f"🔌 봇 로그인됨: {self.user}")
