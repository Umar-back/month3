from aiogram import types, Router, F
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    # print(message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Наш сайт', url='https://python.org'
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Наш инстаграм',url='https://www.instagram.com/lrrixxz/'
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='О нас', callback_data='about'
                )
            ]
        ]
    )

    await message.reply(f'Hello, {message.from_user.first_name}', reply_markup=kb) #reply  отвечает именно на то сообщение message просто ответ

@start_router.callback_query(F.data=='about')
async def show_about_us(call: types.CallbackQuery):
    # await call.answer()
    await call.message.answer('backend')
