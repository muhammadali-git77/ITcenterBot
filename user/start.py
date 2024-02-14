from loader import dp

from utils import texts, buttons
from aiogram import types

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # print(message.chat.id)
    text = texts.START
    await message.answer(text.format(first_name=message.from_user.first_name), reply_markup=buttons.MENU)
