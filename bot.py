
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_button = KeyboardButton("Начать")
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(start_button)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("Узнать кто представитель клуба КГЖ")
main_menu.add("Подписаться на соцсети представителя")
main_menu.add("Поддержать представителя в голосовании")

@dp.message_handler(commands=['start'])
@dp.message_handler(Text(equals="Начать", ignore_case=True))
@dp.message_handler(Text(equals=["Привет", "Start", "Что делать?"], ignore_case=True))
async def send_welcome(message: types.Message):
    await message.answer(
        "Добрый день! Я помощник Клуба Городского Жителя - сокращенно КГЖ. Выбери один из 3-х пунктов",
        reply_markup=main_menu
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
