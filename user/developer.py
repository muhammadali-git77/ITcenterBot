from loader import dp
from utils import texts, buttons
from aiogram import types

@dp.callback_query_handler(text_contains='developer')    
async def callback(callback_data: types.CallbackQuery):
    text = texts.DOM
    await callback_data.message.edit_text(text,reply_markup=buttons.BACK)