from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.default.menu import menu
from keyboards.default.menuKadr import menuKadr
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup = menu)

@dp.message_handler(text="📇Kadrlar bo'limi")
async def send_link(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup = menuKadr)

@dp.message_handler(text="📊Kadrlar uchun eng foydali gruppa va kanallar")
async def send_link(message: Message):
    await message.answer(f"Juda ham foydali ma'lumotlar!")
    await message.answer(f"https://t.me/kadrovikiuzbekistana")
    await message.answer(f"https://t.me/OtdelKadrovUz")
    await message.answer(f"https://t.me/yuristkadrguruhi")

@dp.message_handler(text="Mexnat.uz va O'zbekiston kasaba uyushmalari Federatsiyasi")
async def send_link(message: Message):
    await message.answer(f"1. Тизимга кириш учун (Вход в систему): my.mehnat.uz\n"
                          f"2. Йўриқнома (Инструкция): https://my.mehnat.uz/help"
                            f" 3. Видеоқўлланма (Видео-ролики): https://t.me/YMMT_VIDEO_ENST_Bot"
                            f"4. Телеграм группаси (телеграм-группа):https://t.me/joinchat/URlLmDSe1CID_05m")
    await message.answer(f"https://t.me/my_mexnat_uz")
    await message.answer(f"https://t.me/uzkufk")

@dp.message_handler(text="📂Xujjatlarning na'munalari va to'plami")
async def send_link(message: Message):
    await message.answer(f"https://t.me/OtdelKadrovUzArhiv")

@dp.message_handler(text="Eng top o'quv markazlari va o'qituvchilar")
async def send_link(message: Message):
    await message.answer(f'"YURIST VA KADR" NTM oʻquv markazi\n'
                         f'Рўйҳатдан ўтиш учун телефонлар:'
                         f'☎️ 97-731-40-30, 90-010-86-15')
    await message.answer(f"Bu bo'limga eng ishonchli va sidqi dildan dars beradigan o'quv markazlari va o'qituvchilar haqida ma'lumot joylaymiz, agarda sizda taklif bo'lsa adminga mu'rojaat qiling)https://t.me/frilanserbux")

@dp.message_handler(text="Ish o'rinlari va rezuyu")
async def send_link(message: Message):
        await message.answer(f"http://t.me/vakansiikadri")

@dp.message_handler(text="Bosh sarlavhaga")
async def send_link(message: Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=menu)


