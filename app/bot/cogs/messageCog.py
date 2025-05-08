import re

from discord.ext import commands


class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith(self.bot.command_prefix):
            return

        content = message.content.lower()

        if re.search(r"\b(ㅈㅈ|ww|gg)\b", content):
            await message.channel.send("ㅈㅈ!")


async def setup(bot):
    await bot.add_cog(MessageCog(bot))
