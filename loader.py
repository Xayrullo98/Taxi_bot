from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

"""
ADMINS=6570924683
BOT_TOKEN=6426157215:AAFMYm8sL7UwmYhPMKZVSsBGX0H2N3mSUvg
ip=localhost


"""
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
