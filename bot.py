#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='5686197726:AAGYrzejCKgE9so4kVEgxI8paQLdk1eHLv0')
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp)