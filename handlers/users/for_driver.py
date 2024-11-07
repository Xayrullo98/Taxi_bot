import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from states.customer import CustomerState
from states.driver import DriverState
from keyboards.default.menu import kontakt_buttons, haydovchi_buttons
from loader import dp, bot, base
from aiogram.types import ContentTypes
from keyboards.default.menu import models_


# Echo bot
@dp.callback_query_handler(text_contains="driver")
async def bot_echo(message: types.CallbackQuery):
    await bot.send_message(chat_id=message.from_user.id, text="Telefon no'meringizni kiriting",
                           reply_markup=kontakt_buttons)
    await DriverState.phone.set()


@dp.message_handler(state=DriverState.phone, content_types=ContentTypes.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data({"phone": phone})
    car_models = await models_()
    await bot.send_message(chat_id=message.from_user.id, text="Avtomobilingiz nomini kiriting", reply_markup=car_models)
    await DriverState.model.set()


@dp.message_handler(state=DriverState.model)
async def bot_echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    phone = data.get('phone')
    model = message.text
    fullname = message.from_user.full_name
    username = message.from_user.username
    tg_id = message.from_user.id
    date = datetime.datetime.now()
    status = True
    try:
        base.add_drivers(fullname=fullname,type=1,model=model, tg_id=tg_id, tel=phone, created_at=date, username=username, status=status)
    except Exception:
        pass
    await bot.send_message(chat_id=tg_id, text="Haydovchi sifatda ro'yhatdan o'tdingiz", reply_markup=haydovchi_buttons)
    await state.finish()


@dp.message_handler(state=DriverState.phone)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    if len(text) < 9 or len(text) > 13:
        await message.answer(text="No'merni faqat (XXYYYYYYY)da kiriting")
        await DriverState.phone.set()

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
        await bot.send_message(chat_id=tg_id, text="Haydovchi sifatda ro'yhatdan o'tdingiz",
                               reply_markup=haydovchi_buttons)
        await state.finish()
    else:
        await message.answer(text="No'merni faqat (XXYYYYYYY)da kiriting")
        await DriverState.phone.set()
