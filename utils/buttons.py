
from aiogram import types
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

BACK = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton("Ortga",callback_data="back")]
])

MENU = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Kurslarga qo'shilish",callback_data="ADD")],
        [InlineKeyboardButton("Kurslar haqida", callback_data="course")],
        [InlineKeyboardButton("IT haqida", callback_data="about_itc")],
        [InlineKeyboardButton("Dasturchi xodimlar (ustozlar)",callback_data="developer")]
    ]
)
REGISTER = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [ 
        InlineKeyboardButton("Ortga",callback_data="back"),
        InlineKeyboardButton("Kurslarga Yozilish",callback_data="set"),
        ],
        ]
    )

REGISTER2 = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("To'g'irlash",callback_data="set"),
        InlineKeyboardButton("ITC kanaliga yuborish",callback_data="forward")
        ]
    ]
)
