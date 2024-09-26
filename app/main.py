from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import cfg
from app.handlers import setup_handlers
from app.utils.logger import setup_logger


async def setup(dp):
    setup_logger(cfg.logger_level)

    # db = PostgresDAO(cfg.database_url.get_secret_value())
    # await db.create_db()
    # await db.commit()

    setup_dialogs(dp)
    setup_handlers(dp)


async def main():
    bot = Bot(token=cfg.bot_token.get_secret_value())
    dp = Dispatcher(storage=MemoryStorage())
    await setup(dp)
    await dp.start_polling(bot)
