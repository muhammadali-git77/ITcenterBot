from aiogram import executor
from loader import dp

import user
# from user import start, add, course, register, SetRegister


executor.start_polling(dp, skip_updates=True)