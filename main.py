import asyncio
from aiogram.types import BotCommand
import logging
import sys
from bot import dp, bot

from handlers.start import start_router
from handlers.echo import echo_router
# from handlers.pic import pic_router
from handlers.shop import shop_router

async def main():
    await bot.set_my_commands(
        [
        BotCommand(command='start', description='Главная'),
        BotCommand(command='pic', description='Картинка')
        ])
    # роутеры
    dp.include_router(start_router)
    dp.include_router(shop_router)
    # dp.include_router(pic_router)

    # в самый конец
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
