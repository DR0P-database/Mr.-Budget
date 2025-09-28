from aiogram import Router, types

user_router = Router()

@user_router.message()
async def handle_any_message(message: types.Message): 
    await message.answer("Я еще не обучен многому, но скоро научусь!")