from aiogram import Dispatcher
import asyncio
from lese_handlers import lese_router
from command_handlers import ch_router
from start_menu import set_main_menu
from bot_instance import bot
from FSM import redis_storage
from database import init_models


async def main():
    await init_models()

    dp = Dispatcher(storage=redis_storage)
    dp.startup.register(set_main_menu)
    await set_main_menu(bot)
    dp.include_router(ch_router)
    dp.include_router(lese_router)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())



