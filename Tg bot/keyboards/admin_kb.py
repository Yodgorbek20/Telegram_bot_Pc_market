from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
admin_panel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🆕 Mahsulot qo‘shish", callback_data="add_product")],
    [InlineKeyboardButton(text="📦 Buyurtmalar", callback_data="view_orders")]
])