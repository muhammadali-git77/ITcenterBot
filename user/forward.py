from loader import dp,bot,storage
from utils import texts, buttons
from aiogram import types
from states import Royxat
from aiogram.dispatcher import FSMContext
import os

from .register.tel import step1

@dp.callback_query_handler(text_contains='forward', state="*")
async def callback_edit_result(callback_query: types.CallbackQuery, state: FSMContext):
    
    file_path = f"{callback_query.message.chat.id}.txt"

    try:
        with open(file_path, 'rb') as result_file:
            result_text = result_file.read().decode('utf-8')

    except PermissionError:
        print("PermissionError: Fayl boshqa protsess tomonidan ishlatilmoqda")
        return

    result_file.close()
    
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error while deleting file: {e}")

    await bot.send_message(chat_id="-1002059254116", text=result_text)
    
    await callback_query.message.delete()
    await callback_query.message.answer("Sizning ma'lumotlaringiz ITC Beshariq kanaligayuborildi🚀\nTez orada siz bilan bog'lanamiz!",reply_markup=buttons.MENU)