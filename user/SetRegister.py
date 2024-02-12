from loader import dp
from utils import texts, buttons
from aiogram import types

from states import Royxat

@dp.message_handler(commands="register",state=None)
async def register(message: types.Message):
    await message.answer("👨‍💼Familiya ismingizni kiriting")
    await Royxat.ism.set()
    