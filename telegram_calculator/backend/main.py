import asyncio
import logging
import sys

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN
from app.web.app import create_web_app
from app.bot.handlers import router as bot_router

async def main() -> None:
    """
    Главная асинхронная функция для запуска бота и веб-сервера.
    """
    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Включаем роутер с обработчиками команд
    dp.include_router(bot_router)

    # Создаем экземпляр веб-приложения
    web_app = create_web_app()
    runner = web.AppRunner(web_app)
    await runner.setup()
    
    # Задаем хост и порт для веб-сервера.
    # 0.0.0.0 означает, что сервер будет доступен со всех сетевых интерфейсов.
    site = web.TCPSite(runner, host="0.0.0.0", port=8031)
    
    try:
        # Запускаем веб-сервер
        await site.start()
        logging.info("Веб-сервер запущен на http://0.0.0.0:8031")
        
        # Запускаем опрос Telegram (polling)
        await dp.start_polling(bot)
    finally:
        # Корректное завершение работы
        await runner.cleanup()
        await bot.session.close()


if __name__ == "__main__":
    # Настраиваем логирование для вывода информации в консоль
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Запускаем основную функцию
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")