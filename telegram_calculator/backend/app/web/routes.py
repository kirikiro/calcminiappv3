import aiohttp
from aiohttp import web
from pathlib import Path

# Определяем путь к директории, в которую будет собран наш frontend.
# Мы предполагаем, что папка `frontend/dist` будет находиться на два уровня
# выше относительно текущего файла.
# ВАЖНО: Эта папка появится только ПОСЛЕ сборки frontend-проекта.
STATIC_DIR = Path(__file__).parent.parent.parent.parent / "frontend" / "dist"

async def index(request: web.Request) -> web.Response:
    """
    Обработчик для корневого URL.
    Отдает главный файл `index.html` нашего Vue-приложения.

    :param request: Объект запроса aiohttp.
    :return: Ответ с файлом index.html.
    """
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        # Возвращаем ошибку 503, если фронтенд еще не собран
        return web.Response(
            text="Сервис временно недоступен. Frontend не собран.", 
            status=503
        )
    return web.FileResponse(index_path)

def setup_routes(app: web.Application):
    """
    Настраивает маршруты для веб-приложения aiohttp.

    :param app: Экземпляр aiohttp.web.Application.
    """
    # Маршрут для корневой страницы, отдает index.html
    app.router.add_get("/", index)

    # Маршрут для раздачи статических файлов (JS, CSS, изображения и т.д.)
    # Это позволяет браузеру запрашивать файлы вроде /assets/index-*.js
    app.router.add_static("/", path=STATIC_DIR, name="static")