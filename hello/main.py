from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
import keyboard

import logging


storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти
logging.basicConfig(filename="log.txt",
                    format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s",
                    level=logging.INFO)


@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    joinedFile = open("user.txt", "r")
    joinedUsers = set()

    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},* Бот работает",
                           reply_markup=keyboard.start, parse_mode="Markdown")
    await message.answer("Выберите ссылку:", reply_markup=keyboard.inline_keyboard)


@dp.message_handler(content_types=["text"])
async def get_message(message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id,
                               text="Информация:\nБот создан специально для обучения",
                               parse_mode="Markdown")
    if message.text == "Статистика":
        await bot.send_message(message.chat.id,
                               text="Статистика:\nЗдесь будет статистика",
                               parse_mode="Markdown")


if __name__ == "__main__":
    print("Бот запущен")
    executor.start_polling(dp, skip_updates=True)
