from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp

from states import Royxat

@dp.message_handler(state=Royxat.ism)
async def step1(message: types.Message,state: FSMContext):
    ism = message.text
    length = ism.split()
    
    if len(length) !=2:
        await message.reply("❗️Xatolik : Ismingiz yoki familiyangizni kiritmadingiz\n  Iltimos qaytadan kiriting!")
    else:
        await state.update_data({"ism":ism})
        await message.answer("🕑Iltimos yoshingizni kiriting")
        await Royxat.next()
    