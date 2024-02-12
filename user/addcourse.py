from loader import dp
from utils import texts, buttons
from aiogram import types
from states import Royxat
@dp.callback_query_handler(text_contains='set')    
async def callback(callback_data: types.CallbackQuery):
    text = texts.ADD
    
    await callback_data.message.edit_text("👨‍💼Familiya ismingizni kiriting")
    await Royxat.ism.set()