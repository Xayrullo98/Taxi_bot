import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from states.customer import CustomerState
from keyboards.default.menu import kontakt_buttons, yolovchi_buttons
from loader import dp, bot, base
from aiogram.types import ContentTypes


# Echo bot
@dp.callback_query_handler(text_contains="customer")
async def bot_echo(message: types.CallbackQuery):
    await bot.send_message(chat_id=message.from_user.id, text="Telefon no'meringizni kiriting",
                           reply_markup=kontakt_buttons)
    await CustomerState.phone.set()


@dp.message_handler(state=CustomerState.phone, content_types=ContentTypes.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    fullname = message.from_user.full_name
    username = message.from_user.username
    tg_id = message.from_user.id
    date = datetime.datetime.now()
    status = True
    try:
        base.add_user(fullname=fullname, tg_id=tg_id, tel=phone, created_at=date, username=username, status=status)
    except Exception as x:
        print(x)
    await bot.send_message(chat_id=tg_id, text="Yo'lovchi sifatda ro'yhatdan o'tdingiz", reply_markup=yolovchi_buttons)
    await state.finish()


@dp.message_handler(state=CustomerState.phone)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    if len(text)<9 or len(text)>13:
        await message.answer(text="No'merni faqat (XXYYYYYYY)da kiriting")
        await CustomerState.phone.set()

    elif '93' in text \
            or '94' in text \
            or "90" in text \
            or "91" in text \
            or "33" in text \
            or "88" in text \
            or "95" in text \
            or "97" in text \
            or "98" in text \
            or "99" in text \
            or "71" in text \
            or "50" in text \
            or "20" in text \
            or "78" in text:
        fullname = message.from_user.full_name
        username = message.from_user.username
        tg_id = message.from_user.id
        date = datetime.datetime.now()
        status = True
        try:
            base.add_user(fullname=fullname, tg_id=tg_id, tel=text, created_at=date, username=username, status=status)
        except Exception:
            pass
        await bot.send_message(chat_id=tg_id,text="Yo'lovchi sifatda ro'yhatdan o'tdingiz",reply_markup=yolovchi_buttons)
        await state.finish()
    else:
        await message.answer(text="No'merni faqat (XXYYYYYYY)da kiriting")
        await CustomerState.phone.set()
