from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_buttons)


@dp.message_handler(content_types='video')
async def bot_start(message: types.Message):
    await message.video.download()
    print(message.video, 'dddddddddd')
