from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp

from states import Royxat

@dp.message_handler(state=Royxat.kurs)
async def step1(message: types.Message,state: FSMContext):
    kurs = message.text
    if kurs == "1":
        kurs = "Kompyuter savodxonligi"
    elif kurs == "2":
        kurs = "Web dasturlash"
    elif kurs == "3":
        kurs = "Android ilovalar"
        
       
    await state.update_data({"kurs":kurs})
    await message.answer("📞Iltimos tel raqamingizni kiriting")
    await Royxat.next()