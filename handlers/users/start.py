from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_buttons,yolovchi_buttons,haydovchi_buttons
from loader import dp,base


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = base.select_user(tg_id=message.from_user.id)
    driver = base.select_drivers(tg_id=message.from_user.id)
    if user:
        await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=yolovchi_buttons)
    elif driver:
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=haydovchi_buttons)
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)



