from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import user, admin

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(user.router, admin.router)

async def on_startup():
    print("Bot ishga tushdi")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot, on_startup=on_startup))
