import asyncio
from aiogram import Bot, Dispatcher

bot = Bot(token = '')  # Создаем самого бота
dp = Dispatcher()  # Обработчик всех сообщений и тп бота


async def main():
    await dp.start_polling(bots = bot)  # Запускаем бота и слушаем сервер ТГ


asyncio.run(main())  # Запускаем асинхронно функцию