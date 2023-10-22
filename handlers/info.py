@dp.message(Command('info'))
async def start(message: types.Message):
    print(message)
    await message.answer('My name is Umar')

