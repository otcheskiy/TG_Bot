import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.filters import CommandStart, Command
import logging

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    #print(CommandStart.commands)
    await message.answer( text = f"Привет, {message.from_user.full_name}" )

@dp.message(Command('help'))
async def handle_help(message: types.Message):
    text = 'Я эхо бот.\nОтправь мне сообщение!'
    await message.answer(text = text)

@dp.message()
async def echo(message: types.Message):
    text = message.text
    print(text)
    #text = f"Привет, {message.from_user.full_name}"
    if text in [ 'Привет', 'привет', 'hi', 'hello', 'Hello']:
        await message.answer( text = f"И тебе привет!, {message.from_user.full_name}" )
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer( text = f"До новых встреч, {message.from_user.last_name}")
    else:
        await message.answer(text)





async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

asyncio.run(main())