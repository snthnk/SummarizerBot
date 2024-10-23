from dataclasses import dataclass
from environs import Env

# Описание структуры данных для хранения информации о Telegram боте
@dataclass
class TgBot:
    token: str  # Токен для взаимодействия с API Telegram

# Описание структуры конфигурации приложения
@dataclass
class Config:
    tg_bot: TgBot  # Экземпляр TgBot, содержащий конфигурацию бота

# Функция для загрузки конфигурации из файла окружения (.env)
def load_config(path: str = None) -> Config:
    """Загружает конфигурацию бота из файла окружения.

    Args:
        path (str, optional): Путь до файла .env. Если не указан, используется путь по умолчанию.

    Returns:
        Config: Объект с конфигурацией, содержащий токен бота.
    """
    env = Env()  # Создаем объект для работы с переменными окружения
    env.read_env(path)  # Читаем переменные из указанного .env файла

    # Возвращаем объект Config, содержащий токен бота
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')  # Получаем токен бота из переменных окружения
        )
    )
