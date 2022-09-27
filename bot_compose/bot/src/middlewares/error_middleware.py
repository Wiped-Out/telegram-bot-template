from aiogram import types
from aiogram.utils.exceptions import (BotBlocked, MessageCantBeDeleted,
                                      MessageCantBeEdited, MessageNotModified,
                                      TelegramAPIError)
from core.config import logger
from loader import dp


@dp.errors_handler()
async def errors_handler(update: types.update.Update, exception: Exception):
    """Exceptions handler. Catches all exceptions within task factory tasks."""
    if isinstance(exception, MessageNotModified):
        return True

    if isinstance(exception, BotBlocked):
        return True

    if isinstance(exception, MessageCantBeEdited):
        return True

    if isinstance(exception, MessageCantBeDeleted):
        return True

    if isinstance(exception, TelegramAPIError):
        logger.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logger.exception(f'Update: {update} \n{exception}')
