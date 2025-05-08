from discord.ext import commands


class GreetCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="안녕", help="인사합니다.")
    async def hello(self, ctx):
        await ctx.send("안녕하세요! 👋")


async def setup(bot):
    await bot.add_cog(GreetCog(bot))
