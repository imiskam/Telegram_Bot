from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для обычных кнопок
info = types.KeyboardButton("Информация")
stats = types.KeyboardButton("Статистика")

inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
info1 = InlineKeyboardButton(text="Python Development Info",
                             url="https://pythonist.ru/")
info2 = InlineKeyboardButton(text="Python Test Authomation Info",
                             url="https://habr.com/ru/companies/otus/articles/560884/")

start.add(stats, info)  # добавление кнопок в основу клавиатуры
inline_keyboard.add(info1, info2)  # добавление inline кнопок
