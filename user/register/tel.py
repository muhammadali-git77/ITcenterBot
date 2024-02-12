  
from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp
from states import Royxat
import asyncio
@dp.message_handler(state=Royxat.tel)
async def step1(message: types.Message,state: FSMContext):
    yosh = message.text
    link = message.from_user.username
   
    
    if link == None:
        link = "Username none!"
    await state.update_data({"tel":yosh})
    data = await state.get_data()

    xabar = f"  👨‍💼Familiya ismi : {data.get('ism')}\n  🕑Yoshi : {data.get('yosh')}\n  📚Kurs : {data.get('kurs')}\n  📞Tel raqami: {data.get('tel')}\n  ✈️Telegram username : @{link}"
    
    
    await message.answer(f"Xabar ITC kanaliga yuborildi✅\n\nSizning ma'lumotlaringiz :\n\n{xabar}",reply_markup=buttons.REGISTER2)
    await state.finish()
    
    with open(f'{message.chat.id}.txt', "w", encoding='utf-8') as file:
        file.write(f"O'quvchi haqida ma'lumot:\n\n{xabar}\n\n\n📝Ro'yxatdan o'tish uchun👇👇\n\n   @itcbeshariqbot_bot")
    