import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
from handlers import user_handlers

# Инициализация логгера для логирования событий бота
logger = logging.getLogger(__name__)


# Основная функция для запуска бота
async def main():
    """Основная функция для запуска Telegram бота."""
    
    # Загрузка конфигурации бота из файла окружения
    config: Config = load_config('config_data/.env')
    
    # Инициализация объекта Bot с токеном из конфигурации
    bot = Bot(token=config.tg_bot.token)
    
    # Инициализация памяти для состояний FSM
    storage = MemoryStorage()
    
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'  # Формат сообщений лога
    )
    
    logger.info('Starting bot')  # Сообщение о запуске бота

    # Создание диспетчера с использованием хранилища состояний
    dp = Dispatcher(storage=storage)

    # Подключение роутеров из модуля user_handlers
    dp.include_router(user_handlers.router)

    # Удаление вебхуков и очистка ожидающих обновлений
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запуск долгосрочного опроса сервера Telegram
    await dp.start_polling(bot)

# Запуск главной функции с помощью asyncio
asyncio.run(main())
