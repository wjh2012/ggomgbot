import logging

from discord.ext import commands
from discord import Intents
from openai import AsyncOpenAI

from app.config.env_config import Settings, get_settings
from app.infrastructure.openai.openai_client import OpenAiClient
from app.application.chat_service import ChatService
from app.infrastructure.discord.bot_controller import DiscordBotController
from app.application import BotService
from app.domain.interface import DiscordBotAdapter


def configure_logging(level: str):
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def build_gpt_port(settings: Settings):
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    return OpenAiClient(client)


def build_chat_service(gpt_port):
    return ChatService(gpt=gpt_port)


def build_bot_controller():
    return DiscordBotController()


def build_bot_service(bot_controller):
    return BotService(bot_port=bot_controller)


def build_discord_bot(
    chat_service: ChatService,
    bot_service: BotService,
) -> DiscordBotAdapter:
    intents = Intents.default()
    intents.message_content = True

    bot = DiscordBotAdapter(
        command_prefix="!",
        help_command=commands.DefaultHelpCommand(),
        intents=intents,
        chat_service=chat_service,
        bot_service=bot_service,
    )
    return bot


async def run_bot():
    # 1. Settings
    settings = get_settings()

    # 2. Logging
    logger = logging.getLogger("ggomgbot")
    logger.info("Starting builder...")

    # 3. Compose hexagonal layers
    gpt_port = build_gpt_port(settings)
    chat_service = build_chat_service(gpt_port)
    bot_controller = build_bot_controller()
    bot_service = build_bot_service(bot_controller)
    bot = build_discord_bot(chat_service, bot_service)

    # 4. Adapter ↔ Controller 연결
    bot_controller.set_bot(bot)

    # 5. Discord 시작
    try:
        logger.info("🔌 디스코드 봇 연결 중…")
        await bot.start(settings.discord_bot_token)
    except KeyboardInterrupt:
        logger.info("프로그램이 종료됩니다.")
    except Exception:
        logger.exception("치명적 에러 발생:")
    finally:
        await bot.close()
        logger.info("봇 종료 완료.")
