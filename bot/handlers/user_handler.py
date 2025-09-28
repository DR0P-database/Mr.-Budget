from aiogram import Router, types
from aiogram.filters import Command

user_router = Router()

@user_router.message()
async def handle_any_message(message: types.Message): 
    await message.answer("Я еще не обучен многому, но скоро научусь!")

@user_router.message(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Вот ваше меню!")