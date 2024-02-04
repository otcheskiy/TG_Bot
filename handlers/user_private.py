from aiogram import F, types, Router
#from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    """await message.answer( text = f"Привет, {message.from_user.full_name}, я виртуальный помощник",
                         reply_markup=reply.test_kb )"""
    await message.answer( text = f"Привет, {message.from_user.full_name}, я виртуальный помощник",
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что Вас интересует ?') )

@user_private_router.message(Command('help'))
async def handle_help(message: types.Message):
    text = 'Я эхо бот.\nОтправь мне сообщение!'
    await message.answer(text = text)


# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message( or_f (Command('menu'), (F.text.lower() == 'меню' ) ))
async def handle_menu(message: types.Message):
    text = 'Вот меню:'
    await message.answer(text = text, reply_markup=reply.del_kbd)


@user_private_router.message(F.text.lower() == 'о магазине')
@user_private_router.message(Command('about'))
async def handle_about(message: types.Message):
    text = '<b><i>О магазине: </i></b>'
    await message.answer(text)

@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payments'))
async def handle_payment(message: types.Message):
    text = as_marked_section(
            Bold('Варианты оплаты:'),
            'Картой в боте',
            'При получении',
            'В заведении',
            marker='✅ '
                )
    await message.answer(text.as_html())

@user_private_router.message(
        (F.text.lower().contains('доставка')) | (F.text.lower() == 'варианты доставки')
)
@user_private_router.message(Command('shipping'))
async def menu_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='❌ '
        ),
        sep='\n----------------------\n'
    )
    await message.answer(text.as_html())

@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact.phone_number))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"локация получена")
    await message.answer(str(message.location))

@user_private_router.message(F.photo)
async def menu_cmd(message: types.Message):
    text = 'Это магический фильтр'
    await message.answer(text = text)

@user_private_router.message(F.text)
async def echo(message: types.Message):
    text_low = message.text.lower()
    text = message.text
    if text_low in [ 'привет', 'здорово', 'здравствуйте', 'hi', 'hello']:
        await message.answer( text = f"И тебе привет!, {message.from_user.full_name}" )
    elif text_low in ['пока', 'до свидания']:
        await message.answer( text = f"До новых встреч, {message.from_user.last_name}")
    else:
        await message.answer(text)