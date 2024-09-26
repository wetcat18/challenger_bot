from aiogram import Router, Dispatcher
from aiogram.enums import ParseMode
from aiogram_dialog import DialogManager, Dialog, Window
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog.widgets.kbd import Group, Start
from aiogram_dialog.widgets.text import Const

from app.config import cfg
from app.states import user_states as states


start_router = Router()


@start_router.message(CommandStart())
async def send_welcome(message: Message, dialog_manager: DialogManager):
    if message.from_user.id == cfg.user_id:
        await dialog_manager.start(state=states.MainMenu.MAIN)
    else:
        await message.answer("<b>❌ Отказано в доступе!</b>")


main_menu_dialog = Dialog(
    Window(
        Const('<b>📋 Главное меню</b>'),
        Group(
            Start(
                Const('⚡ Задания на сегодня'),
                id='daily_tasks',
                state=
            ),
            Start(
                Const('🗓️ Сегодняшний график'),
                id='daily_tasks',
                state=
            ),
            width=2
        ),
        Group(
            Start(
                Const('Расписания'),
                id='daily_tasks',
                state=
            ),
            Start(
                Const('🗓️ Сегодняшний график'),
                id='daily_tasks',
                state=
            ),
            width=2
        ),
        state=states.MainMenu.MAIN,
        parse_mode=ParseMode.HTML
    )
)


def setup_start(dp: Dispatcher) -> None:
    dp.include_routers(start_router, main_menu_dialog)
