from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

from loader import base

menu_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍💼Men yo'lovchiman",callback_data='customer'),
            InlineKeyboardButton(text="🚖Men haydovchiman",callback_data='driver'),
        ]
    ]

)

kontakt_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text="Kontakt yuborish",request_contact=True),
        ]
    ],
    resize_keyboard=True
)

yolovchi_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buyurtma berish"),

        ],
        [
            KeyboardButton(text="Buyurtmalarim"),
            KeyboardButton(text="⚙️Sozlamalar"),
        ]
    ],
    resize_keyboard=True
)

haydovchi_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Reys yaratish"),

        ],
        [
            KeyboardButton(text="Mening Reyslarim"),
            KeyboardButton(text="Sozlamalar"),
        ]
    ],
    resize_keyboard=True
)


async def models_():
    car_models = base.select_all_models()
    index = 0
    keys = []
    j = 0
    for model in car_models:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{model[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{model[1]}', ))
        j += 1

    # keys.append([KeyboardButton(text="Ortga")])
    course_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return course_buttons


async def regions():
    car_models = base.select_all_regions()
    index = 0
    keys = []
    j = 0
    for model in car_models:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{model[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{model[1]}', ))
        j += 1

    # keys.append([KeyboardButton(text="Ortga")])
    course_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return course_buttons

number_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),

        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),

        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),

        ]
    ],
    resize_keyboard=True
)

confim_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash",callback_data='confirm'),
            InlineKeyboardButton(text="Bekor qilish",callback_data='cancel'),
        ]
    ]

)

driver_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Haydovchi sifatida kirish",callback_data='haydovchi'),

        ]
    ]

)

passenger_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yo'lovchi sifatida kirish", callback_data='yolovchi'),

        ]
    ]

)