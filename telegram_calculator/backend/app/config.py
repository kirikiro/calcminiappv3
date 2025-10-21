import os
from pathlib import Path
from dotenv import load_dotenv

# Определяем путь к файлу .env
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Загружаем токен бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен был загружен
if not BOT_TOKEN:
    raise ValueError("Необходимо указать BOT_TOKEN в .env файле")

# URL  веб-приложения.
WEB_APP_URL = "https://open-comics-enjoy.loca.lt"