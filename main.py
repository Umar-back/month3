import asyncio
import logging
import sys
# from decouple import config
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message(Command('start'))
async def start(message: types.Message):
    print(message.from_user)
    await message.reply(f'Hello, {message.from_user.first_name}') #reply  отвечает именно на то сообщение message просто ответ

@dp.message(Command('pic'))
async def pic(message: types.Message):
    file = types.FSInputFile('images/photo1.jpg')
    await message.answer_photo(file)

@dp.message(Command('info'))
async def start(message: types.Message):
    print(message)
    await message.answer('My name is Umar')


# @dp.message()
# async def echo(message: types.Message):
#     await message.answer(message.text)


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())