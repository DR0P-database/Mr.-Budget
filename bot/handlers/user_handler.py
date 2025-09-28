from aiogram import Router, types
from aiogram.filters import Command

user_chat_router = Router()  # Роутер обрабатывет сообщения в личном чате

@user_chat_router.message()
async def handle_any_message(message: types.Message): 
    await message.answer("Я еще не обучен многому, но скоро научусь!")

@user_chat_router.message(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Вот ваше меню!")