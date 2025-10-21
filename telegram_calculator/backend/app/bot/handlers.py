from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.keyboard import get_calculator_keyboard

# объект Router для обработки сообщений
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение и клавиатуру с кнопкой
    для открытия калькулятора.

    :param message: Объект сообщения от пользователя.
    """
    await message.answer(
        "Привет! Это бот с инженерным калькулятором. "
        "Нажми на кнопку ниже, чтобы открыть его.",
        reply_markup=get_calculator_keyboard()
    )