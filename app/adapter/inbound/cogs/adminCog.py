from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot, bot_service):
        self.bot = bot
        self.bot_service = bot_service

    @commands.command(name="이름변경", help="봇 이름을 변경합니다.")
    async def rename_bot(self, ctx, *, new_name: str):
        await self.bot_service.rename_bot(ctx.guild.id, new_name)
        await ctx.send(f"✅ 봇 닉네임이 '{new_name}'으로 변경되었습니다.")


async def setup(bot):
    await bot.add_cog(AdminCog(bot, bot.bot_service))
