from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import read_db

products = read_db()["products"]
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=prod["name"], callback_data=f"product_{i}")]
    for i, prod in enumerate(products)
])
