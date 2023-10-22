from aiogram import types
from aiogram.filters import Command

pic_router = Router()

@pic_router.message(Command('pic'))
async def pic(message: types.Message):
    file = types.FSInputFile('images/photo1.jpg')
    await message.answer_photo(file)