from loader import dp
from utils import texts, buttons
from aiogram import types

@dp.callback_query_handler(text_contains='about_itc')    
async def callback(callback_data: types.CallbackQuery):
    text = texts.ABOUT_ITC
    await callback_data.message.edit_text(text,reply_markup=buttons.BACK)