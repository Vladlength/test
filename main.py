import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.filters import Command
from aiohttp import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = '7197491181:AAHAUrAYczXlRBqk_FbgsWctz40MKQyhzWE'
WEBHOOK_URL = 'https://test-wfip.onrender.com'  # Замените на ваш домен
PORT = 3000

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

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()

async def handle_webhook(request):
    json = await request.json()
    update = types.Update(**json)
    await dp.feed_update(update)
    return web.Response()

app = web.Application()
app.router.add_post('/webhook', handle_webhook)

if __name__ == '__main__':
    dp.include_router(router)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, port=PORT)