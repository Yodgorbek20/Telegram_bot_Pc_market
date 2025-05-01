from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import ADMINS
from keyboards.admin_kb import admin_panel_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.db import read_db, write_db

router = Router()

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()

@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("🔧 Admin panelga xush kelibsiz!", reply_markup=admin_panel_kb)
    else:
        await message.answer("❌ Sizda ruxsat yo‘q.")

@router.callback_query(F.data == "add_product")
async def start_add_product(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("📝 Mahsulot nomini kiriting:")
    await state.set_state(AddProduct.name)

@router.message(AddProduct.name)
async def set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("💵 Narxini kiriting:")
    await state.set_state(AddProduct.price)

@router.message(AddProduct.price)
async def set_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("🧾 Tavsifini kiriting:")
    await state.set_state(AddProduct.description)

@router.message(AddProduct.description)
async def set_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("🖼 Rasmini yuboring (URL yoki Telegram fayl):")
    await state.set_state(AddProduct.photo)

@router.message(AddProduct.photo)
async def set_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    photo = message.photo[-1].file_id if message.photo else message.text
    db = read_db()
    db["products"].append({
        "name": data["name"],
        "price": data["price"],
        "description": data["description"],
        "photo": photo
    })
    write_db(db)
    await message.answer("✅ Mahsulot muvaffaqiyatli qo‘shildi!")
    await state.clear()

@router.callback_query(F.data == "view_orders")
async def view_orders(callback: CallbackQuery):
    db = read_db()
    if not db["orders"]:
        await callback.message.answer("📭 Buyurtmalar yo‘q.")
    else:
        for order in db["orders"]:
            text = f"👤 Ism: {order['name']}\n📞 Tel: {order['phone']}\n📍 Manzil: {order['address']}\n📦 Mahsulot: {order['product']}"
            await callback.message.answer(text)
