from loader import dp
from utils import texts, buttons
from aiogram import types

@dp.callback_query_handler(text_contains='ADD')    
async def callback(callback_data: types.CallbackQuery):
    text = texts.ADD
    
    await callback_data.message.delete()
    await callback_data.message.answer(text, reply_markup=buttons.REGISTER)