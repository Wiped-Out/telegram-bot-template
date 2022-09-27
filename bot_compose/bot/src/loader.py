from aiogram import Bot, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import Dispatcher
from core.config import settings

bot = Bot(
    token=settings.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
    disable_web_page_preview=True,
)

dp = Dispatcher(
    bot,
    storage=RedisStorage2(host=settings.REDIS_HOST, port=settings.REDIS_PORT),
)
