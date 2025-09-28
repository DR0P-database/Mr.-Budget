from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from bot.settings import get_settings
from bot.handlers.user_handler import user_chat_router
from bot.common.bot_cmds_lst import private_chat_cmds


settings = get_settings()  # Получаем настройки из файла settings.py
bot = Bot(token = settings.TOKEN_BOT)  # Создаем самого бота, который слушает и получает все обновления сервера
dp = Dispatcher()  # Обработчик всех сообщений и тп бота


@dp.message(CommandStart())  # Диспетчер обрабатывает пользовательские сообщения и фильтрует все события
async def message_start_bot(message: types.Message):  # Тип для чтобы понимал что это сообщение
    await message.answer(text="Hello world")

dp.include_router(user_chat_router)

async def start():
    await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем сообщения которые пришли пока бот был оффлайн
    # bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())  # Удаляем команды бота в личке
    bot.set_my_commands(commands=private_chat_cmds, scope=types.BotCommandScopeAllPrivateChats())  # Команды бота в личном чате
    await dp.start_polling(bot, allowed_updates=settings.ALLOWED_UPDATES)  # Запускаем бота и слушаем сервер ТГ