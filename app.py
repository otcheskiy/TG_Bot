#стандартные модули питона
import asyncio
import os

# модули aiogram 
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
#from config import token_tg

import logging
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

#пользовательские модули
from handlers.user_private import user_private_router
from common.bot_cmds_list import private

#print( 'token_tg: ', token_tg)

ALLOWED_UPDATE = ['message, edited_message']

#bot = Bot(token_tg)
bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATE)

asyncio.run(main())