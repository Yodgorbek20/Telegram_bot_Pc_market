from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import read_db, write_db
from keyboards.user_kb import main_menu

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Xush kelibsiz! Kompyuter qismlarini tanlang.", reply_markup=main_menu)

@router.callback_query(F.data.startswith("product_"))
async def show_product(callback: CallbackQuery):
    db = read_db()
    product_id = int(callback.data.split("_")[1])
    product = db["products"][product_id]
    text = f"<b>{product['name']}</b>\nNarxi: {product['price']} so'm\n{product['description']}"
    await callback.message.answer_photo(photo=product['photo'], caption=text)