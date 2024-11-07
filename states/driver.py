from aiogram.dispatcher.filters.state import State, StatesGroup


class DriverState(StatesGroup):
    phone = State()
    model = State()
    confirm = State()


class DriverOrderState(StatesGroup):
    from_place = State()
    to_place = State()
    price = State()
    number = State()
    date = State()
    confirm = State()