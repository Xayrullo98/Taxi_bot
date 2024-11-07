import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.menu import regions, number_buttons, confim_buttons, yolovchi_buttons, driver_buttons, \
    kontakt_buttons
from states.customer import BuyurtmaState
from loader import dp, bot, base


# Echo bot
from states.driver import DriverState


@dp.message_handler(text="Buyurtma berish")
async def bot_echo(message: types.Message):
    regions_button = await regions()
    await message.answer(text="Qayerdan ketmoqchisiz", reply_markup=regions_button)
    await BuyurtmaState.from_place.set()


@dp.message_handler(state=BuyurtmaState.from_place)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({"from_place": message.text})
    regions_button = await regions()
    await message.answer(text="Qayerga bormoqchisiz", reply_markup=regions_button)
    await BuyurtmaState.to_place.set()


@dp.message_handler(state=BuyurtmaState.to_place)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({"to_place": message.text})
    await message.answer(text="Odamlar sonini kiriting", reply_markup=number_buttons)
    await BuyurtmaState.number.set()


@dp.message_handler(state=BuyurtmaState.number)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data({"number": message.text})
        await message.answer(text="Qanchadan Ketmoqchisiz (so'mda kiriting M:100ming so'm)",
                             reply_markup=ReplyKeyboardRemove())
        await BuyurtmaState.price.set()
    else:
        await message.answer(text="Odamlar sonini faqat raqamda kiriting", reply_markup=number_buttons)
        await BuyurtmaState.number.set()


@dp.message_handler(state=BuyurtmaState.price)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({"price": message.text})
    await message.answer(text="Qachon Ketmoqchisiz",
                         reply_markup=ReplyKeyboardRemove())
    await BuyurtmaState.date.set()


@dp.message_handler(state=BuyurtmaState.date)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({"date": message.text})
    data = await state.get_data()
    from_place = data.get('from_place')
    to_place = data.get('to_place')
    number = data.get('number')
    price = data.get('price')
    date = data.get('date')
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=f"{from_place}dan {to_place}ga \n"
                                                 f"👨‍👧‍👦{number}\n"
                                                 f"💰 {price}\n"
                                                 f"🕰 {date}", reply_markup=confim_buttons)
    await bot.send_message(chat_id=user_id, text="Tasdiqlash tugmasini bosing")
    await BuyurtmaState.confirm.set()


@dp.callback_query_handler(state=BuyurtmaState.confirm, text="confirm")
async def bot_echo(message: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    from_place = data.get('from_place')
    to_place = data.get('to_place')
    number = data.get('number')
    price = data.get('price')
    date = data.get('date')
    user_id = message.from_user.id
    created_at = datetime.datetime.now()
    base.add_customer_order(from_place=from_place, to_place=to_place, number=number, tg_id=user_id, date=date,
                            status=True, created_at=created_at, price=price)
    await bot.send_message(chat_id=user_id, text="Buyurtma qabul qilindi", reply_markup=yolovchi_buttons)
    await state.finish()


@dp.callback_query_handler(state=BuyurtmaState.confirm, text="cancel")
async def bot_echo(message: types.CallbackQuery, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Bekor qilindi", reply_markup=yolovchi_buttons)
    await state.finish()


@dp.message_handler(text="Buyurtmalarim")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    buyurtmalar = base.select_customer_orders(tg_id=user_id)

    for buyurtma in buyurtmalar:
        from_place = buyurtma[1]
        to_place = buyurtma[2]
        number = buyurtma[4]
        price = buyurtma[3]
        date = buyurtma[6]
        await bot.send_message(chat_id=user_id, text=f"{from_place} dan {to_place}ga \n"
                                                     f"👨‍👧‍👦 {number} ta\n"
                                                     f"💰 {price}\n"
                                                     f"🕰 {date}", )


@dp.message_handler(text="⚙️Sozlamalar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="O'zgartirish", reply_markup=driver_buttons)


@dp.callback_query_handler(text="haydovchi")
async def bot_echo(message: types.CallbackQuery):
    user_id = message.from_user.id
    base.delete_user(tg_id=user_id)
    await bot.send_message(chat_id=message.from_user.id, text="Telefon no'meringizni kiriting",
                           reply_markup=kontakt_buttons)
    await DriverState.phone.set()
