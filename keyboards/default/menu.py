from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

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
            KeyboardButton(text="⚙️Sozlamalar"),
        ]
    ],
    resize_keyboard=True
)