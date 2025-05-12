import asyncio
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from discord.ext import commands
from discord import Intents
from openai import AsyncOpenAI

from app.config.env_config import get_settings, Settings
from app.adapter.outbound.openai_client_adapter import OpenAiClientAdapter
from app.adapter.outbound.discord_nickname_adapter import DiscordNicknameAdapter
from app.application.chat_service import ChatService
from app.application.bot_service import BotService
from app.adapter.inbound.discord_bot import DiscordBot


def build_openai_adapter(settings: Settings) -> OpenAiClientAdapter:
    """OpenAI API 클라이언트를 생성하고 어댑터로 래핑합니다."""
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    return OpenAiClientAdapter(client)


def build_services(settings: Settings):
    """
    챗 서비스, 봇 서비스, 닉네임 어댑터를 생성하여 반환합니다.
    """
    openai_adapter = build_openai_adapter(settings)
    chat_service = ChatService(openai_adapter)
    nick_adapter = DiscordNicknameAdapter()
    bot_service = BotService(nick_adapter)
    return chat_service, bot_service, nick_adapter


def build_discord_bot(
    chat_service: ChatService,
    bot_service: BotService,
    nick_adapter: DiscordNicknameAdapter,
) -> DiscordBot:
    """
    DiscordBot 인스턴스를 생성하고, 닉네임 어댑터에 봇 인스턴스를 주입합니다.
    """
    intents = Intents.default()
    intents.message_content = True

    bot = DiscordBot(
        command_prefix="!",
        help_command=commands.DefaultHelpCommand(),
        intents=intents,
        chat_service=chat_service,
        bot_service=bot_service,
    )
    # NickNamePort 구현체에 봇 인스턴스 설정
    nick_adapter.set_bot(bot)
    return bot


def main():
    settings = get_settings()
    chat_service, bot_service, nick_adapter = build_services(settings)
    bot = build_discord_bot(chat_service, bot_service, nick_adapter)

    # 봇 시작
    try:
        asyncio.run(bot.start(settings.discord_bot_token))
    except KeyboardInterrupt:
        asyncio.run(bot.close())


if __name__ == "__main__":
    main()
