from aiohttp import web
from app.web.routes import setup_routes

def create_web_app() -> web.Application:
    """
    Создает и настраивает экземпляр веб-приложения aiohttp.

    :return: Настроенный экземпляр aiohttp.web.Application.
    """
    # Создаем основной объект приложения
    app = web.Application()

    # Настраиваем маршруты (URL-адреса)
    setup_routes(app)

    return app