from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from core.config import logger
from db.database import create_database
from loader import dp
from middlewares import dp  # noqa: F811, WPS440

# todo don't forget to import all handlers here


async def on_startup(dispatcher: Dispatcher):
    await create_database()

    logger.info('Bot started')


async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
