from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from app.config import WEB_APP_URL

def get_calculator_keyboard() -> InlineKeyboardMarkup:
    """
    Создает и возвращает инлайн-клавиатуру с кнопкой для открытия
    веб-приложения (Mini App) калькулятора.

    :return: Объект инлайн-клавиатуры.
    """
    # Создаем объект WebAppInfo, указывающий на URL нашего веб-приложения
    web_app_info = WebAppInfo(url=WEB_APP_URL)

    # Создаем кнопку, которая будет открывать наше веб-приложение
    calculator_button = InlineKeyboardButton(
        text="Открыть калькулятор",
        web_app=web_app_info
    )

    # Создаем инлайн-клавиатуру и добавляем в нее нашу кнопку
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[calculator_button]]
    )
    return keyboard