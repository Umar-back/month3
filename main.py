import asyncio
from aiogram.types import BotCommand
import logging
from logging import basicConfig
import sys
from bot import dp, bot

from handlers import (
    start_router,
    shop_router,
    echo_router,
    pic_router,
    questions_router
)

async def main():
    await bot.set_my_commands(
        [
        BotCommand(command='start', description='Главная'),
        BotCommand(command='pic', description='Картинка')
        ]
    )
    await dp.start_polling(bot)
# роутеры
dp.include_router(start_router)
dp.include_router(shop_router)
dp.include_router(pic_router)
dp.include_router(questions_router)

# в самый конец
dp.include_router(echo_router)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
