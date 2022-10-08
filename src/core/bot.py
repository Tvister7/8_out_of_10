from aiogram import Bot, Dispatcher

from .settings import settings

bot = Bot(token=settings.telegram_token)
dp = Dispatcher(bot)
