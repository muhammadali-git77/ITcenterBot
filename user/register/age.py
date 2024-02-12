
from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp

from states import Royxat

@dp.message_handler(state=Royxat.yosh)
async def step1(message: types.Message,state: FSMContext):
    yosh = message.text
    if yosh.isalpha():
        await message.reply("❗️Xatolik : Iltimos raqam kiriting!")
    elif len(yosh) > 2:
        await message.reply("❗️Xatolik : Ikkitadan ortiq raqam kiritib bo'lmaydi\n  Iltimos qayta kiriting!")
    else:    
        await state.update_data({"yosh":yosh})
        await message.answer("Iltimos o'quv kursini kiriting📝\n\nKurslar:\n  1️⃣.Kompyuter savodxonligi\n  2️⃣.Web dasturlash\n  3️⃣.Android ilovalar\n\n❗️Eslatma : 1,2,3 sonlaridan birini,\n  yoki siz yozilmoqchi bo'lgan kursni nomini yozing")
        await Royxat.next()