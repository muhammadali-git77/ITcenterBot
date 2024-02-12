
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6906214666:AAFu50957O2PdUn3k88motJH00IalwIWzEc")
storage=MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())