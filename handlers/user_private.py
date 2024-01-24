from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    #print(CommandStart.commands.__dir__)
    await message.answer( text = f"Привет, {message.from_user.full_name}, я виртуальный помощник" )

@user_private_router.message(Command('help'))
async def handle_help(message: types.Message):
    text = 'Я эхо бот.\nОтправь мне сообщение!'
    await message.answer(text = text)

@user_private_router.message(Command('menu'))
async def handle_menu(message: types.Message):
    text = 'Вот меню:'
    await message.answer(text = text)

@user_private_router.message(Command('about'))
async def handle_about(message: types.Message):
    text = 'О нас:'
    await message.answer(text = text)

@user_private_router.message(Command('payments'))
async def handle_payment(message: types.Message):
    text = 'Варианты оплаты:'
    await message.answer(text = text)

@user_private_router.message(Command('shipping'))
async def handle_payment(message: types.Message):
    text = 'Варианты доставки:'
    await message.answer(text = text)

"""@user_private_router.message()
async def echo(message: types.Message):
    text = message.text
    #print(text)
    #text = f"Привет, {message.from_user.full_name}"
    if text in [ 'Привет', 'привет', 'hi', 'hello', 'Hello']:
        await message.answer( text = f"И тебе привет!, {message.from_user.full_name}" )
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer( text = f"До новых встреч, {message.from_user.last_name}")
    else:
        await message.answer(text)"""

@user_private_router.message(F.photo)
async def menu_cmd(message: types.Message):
    text = 'Это магический фильтр'
    await message.answer(text = text)