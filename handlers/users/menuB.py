from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.default.menu import menu
from keyboards.default.menuBux import menuBux
from loader import dp

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup = menu)

@dp.message_handler(text="🧮Buxgalteriya")
async def send_link(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup = menuBux)


@dp.message_handler(text="📊Eng foydali gruppa va kanallar")
async def send_link(message: Message):
    await message.answer(f"Eng foydali gruppa va kanallar ro'yxati:")
    await message.answer(f"https://t.me/BUXGALTERIYA_1CC")
    await message.answer(f"https://t.me/buxgalter_kerak2")
    await message.answer(f"https://t.me/buhgalteria_uz")
    await message.answer(f"https://t.me/joinchatmentalistuz")
    await message.answer(f"https://t.me/taxuzb")

@dp.message_handler(text="🖥Barchasi 1C haqida")
async def send_link(message: Message):
    await message.answer(f"1C bo'yicha foydali gruppa va kanallar:")
    await message.answer(f"https://t.me/Consultation1C")
    await message.answer(f"https://t.me/buhgalteria_uz_1C")
    await message.answer(f"https://t.me/videokurs_1c")
    await message.answer(f"https://t.me/videokurs_1c/5")
    await message.answer(f"https://t.me/videokurs_1c/6")
    await message.answer(f"https://t.me/videokurs_1c/7")
    await message.answer(f"https://t.me/videokurs_1c/8")
    await message.answer(f"https://t.me/videokurs_1c/19")
    await message.answer(f"https://t.me/videokurs_1c/20")
    await message.answer(f"https://t.me/videokurs_1c/25")
    await message.answer(f"https://t.me/videokurs_1c/27")
    await message.answer(f"https://t.me/videokurs_1c/61")

@dp.message_handler(text="📈Xisobotlar uchun qo'llanmalar")
async def send_link(message: Message):
    await message.answer(f"Акциз солиғи ҳисобот шаклини тўлдириш тартиби бўйича видеоқўлланма:https://youtu.be/qCavynoeBvc?list=PLUxn7yxBg4J1-S5Qz87qo8mlxfM0rE3Nt")
    await message.answer(f"Қўшилган қиймат солиғи ҳисобот шаклини тўлдириш бўйича видеоқўлланма:https://youtu.be/2fx3Hdc-cMk?list=PLUxn7yxBg4J1-S5Qz87qo8mlxfM0rE3Nt")
    await message.answer(f"Практикум: 2022 йил учун Айланмадан солиқ ҳисоботини тўлдириш:https://youtu.be/Y76OrTS_IEM")
    await message.answer(f"Foyda solig‘i hisobotlariga kiritilgan o‘zgarishlar bo‘yicha tushuntirish berish:https://youtu.be/C9npm20UzoU")
    await message.answer(
        f"JShODS va ijtimoiy soliq hisob-kitobini to‘ldirish bo‘yicha videoqo‘llanma:https://youtu.be/XEM95bjdKVY")

@dp.message_handler(text="📂Xujjatlarning na'munalari va to'plami")
async def send_link(message: Message):
    await message.answer(f"Bu bo'lim ishlov jarayonida")

@dp.message_handler(text="📚BXMS va Soliq kodeksi(oxirgi taxriri)")
async def send_link(message: Message):
    await message.answer(f"BXMS:https://lex.uz/nsbu")
    await message.answer(f"Soliq kodeksi:https://lex.uz/docs/4674902")

@dp.message_handler(text="🧑‍🎓Top o'quv markazlari va o'qituvchilar")
async def send_link(message: Message):
    await message.answer(f"Adminga o'zingiz bilgan eng yaxshi o'quv markazlari xaqida ma'lumot yuboring:https://t.me/frilanserbux")

@dp.message_handler(text="🕵️‍♂️Ish o'rinlari")
async def send_link(message: Message):
    await message.answer(f"https://t.me/workbhb")
    await message.answer(f"https://t.me/Buxgalter_kerak1")
    await message.answer(f"https://t.me/buhgalteria_uz_vakansii")
@dp.message_handler(text="Menu")
async def show_menu(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup = menu)
