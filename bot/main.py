from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from bot.settings import get_settings


settings = get_settings()  # Получаем настройки из файла settings.py
bot = Bot(token = settings.TOKEN_BOT)  # Создаем самого бота, который слушает и получает все обновления сервера
dp = Dispatcher()  # Обработчик всех сообщений и тп бота


@dp.message(CommandStart())  # Диспетчер обрабатывает пользовательские сообщения и фильтрует все события
async def message_start_bot(message: types.Message):  # Тип для чтобы понимал что это сообщение
    await message.answer(text="Hello world")

async def start():
    await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем сообщения которые пришли пока бот был оффлайн
    await dp.start_polling(bot)  # Запускаем бота и слушаем сервер ТГ