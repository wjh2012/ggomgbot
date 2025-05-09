from discord.ext import commands


class GptCog(commands.Cog):
    def __init__(self, bot, chat_service):
        self.bot = bot
        self.chat_service = chat_service

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("철수"):
            query = message.content.replace("철수", "", 1).strip()
            response = await self.chat_service.ask(
                user_id=str(message.author.id),
                message=query,
                channel_id=str(message.channel.id),
            )
            await message.channel.send(response)


async def setup(bot):
    await bot.add_cog(GptCog(bot, bot.chat_service))
