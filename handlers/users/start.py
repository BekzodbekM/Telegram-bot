from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart



from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, {message.from_user.full_name}, buxgalter uz botiga xush kelibsiz!\n"
                         f"Bot ishga tushishi uchun /menu buyrug'ini yuboring" )
