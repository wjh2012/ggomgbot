from discord.ext import commands


class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "안녕" in message.content:
            await message.channel.send("안녕하세요!")


async def setup(bot):
    await bot.add_cog(MessageCog(bot))
