import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.filters import CommandStart


bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это старт")

@dp.message()
async def echo(message: types.Message):
    text = message.text

    if text in [ 'Привет', 'привет', 'hi', 'hello', 'Hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer('До новых встреч')
    else:
        await message.answer(message.text)





async def main():
    await dp.start_polling(bot)

asyncio.run(main())