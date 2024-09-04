import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.filters import Command

API_TOKEN = '7197491181:AAHAUrAYczXlRBqk_FbgsWctz40MKQyhzWE'  # Замените 'YOUR_TOKEN' на токен вашего бота

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Открыть карту", url='https://map-umber.vercel.app/')]
    ])
    await message.answer("Привет! Открываю карту:", reply_markup=keyboard)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
