from discord.ext import commands


class CommandBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def setup_hook(self):
        await self.load_extension("app.bot.cogs.greetCog")
        await self.load_extension("app.bot.cogs.messageCog")

    async def on_ready(self):
        print(f"🔌 봇 로그인됨: {self.user}")
