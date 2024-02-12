from loader import dp
from utils import texts, buttons
from aiogram import types

@dp.callback_query_handler(text_contains='back')    
async def callback(callback_data: types.CallbackQuery):
    text = texts.START
    await callback_data.message.edit_text(text,reply_markup=buttons.MENU)