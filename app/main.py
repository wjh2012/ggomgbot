import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio

from app.bot.Client import BotClient

import discord

from app.config.env_config import get_settings

config = get_settings()


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = BotClient(intents=intents)
    await client.start(config.discord_bot_token)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("프로그램이 종료되었습니다.")
