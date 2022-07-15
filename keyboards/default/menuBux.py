from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuBux=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📊Eng foydali gruppa va kanallar"),
        ],
        [
            KeyboardButton(text="🖥Barchasi 1C haqida"),
        ],
        [
            KeyboardButton(text="📈Xisobotlar uchun qo'llanmalar"),
        ],
        [
            KeyboardButton(text="📂Xujjatlarning na'munalari va to'plami"),
        ],
        [
            KeyboardButton(text="📚BXMS va Soliq kodeksi(oxirgi taxriri)"),
        ],
        [
            KeyboardButton(text="🧑‍🎓Top o'quv markazlari va o'qituvchilar"),
        ],
        [
            KeyboardButton(text="🕵️‍♂️Ish o'rinlari"),
        ],
        [
            KeyboardButton(text="Menu"),
        ],
    ],
    resize_keyboard=True
)