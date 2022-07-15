from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuKadr=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📊Kadrlar uchun eng foydali gruppa va kanallar"),
        ],
        [
            KeyboardButton(text="Mexnat.uz va O'zbekiston kasaba uyushmalari Federatsiyasi"),
        ],
        [
            KeyboardButton(text="📂Xujjatlarning na'munalari va to'plami"),
        ],
        [
            KeyboardButton(text="Eng top o'quv markazlari va o'qituvchilar"),
        ],
        [
            KeyboardButton(text="Ish o'rinlari va rezuyu"),
        ],
        [
            KeyboardButton(text="Bosh sarlavhaga"),
        ]
    ],
    resize_keyboard=True
)