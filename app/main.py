import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ai.openai_api.openai_client import OpenAiClient

from discord.ext import commands
from openai import AsyncOpenAI


from app.bot.command_bot import CommandBot

import asyncio

import discord

from app.config.env_config import get_settings

config = get_settings()


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    # bot = ClientBot(intents=intents)
    bot = CommandBot(
        command_prefix="!", help_command=commands.DefaultHelpCommand(), intents=intents
    )
    client = AsyncOpenAI(api_key=config.openai_api_key)
    openai_client = OpenAiClient(client)
    await openai_client.chat()
    # await bot.start(config.discord_bot_token)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("프로그램이 종료되었습니다.")
