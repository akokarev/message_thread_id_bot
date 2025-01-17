from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes,
)
import logging
import traceback
import sys

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Функция для обработки любых ошибок
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Логирует ошибки, возникающие в боте."""
    logger.error("Произошла ошибка: %s", context.error)

# Основная функция обработки сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        chat_id = update.message.chat.id
        thread_id = update.message.message_thread_id

        response = (
            f"Ваш ID: {user_id}\n"
            f"ID группы/чата: {chat_id}\n"
            f"ID треда (если есть): {thread_id}"
        )

        await update.message.reply_text(response)
    except Exception as e:
        logger.error("Ошибка в обработке сообщения: %s", e)

# Функция запуска бота
def main():
    try:
        # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
        application = ApplicationBuilder().token("7144847727:AAFHqEXLWFI9wSqF5wBZtLFpX9jZuZZp9fc").build()

        # Добавляем обработчик сообщений
        application.add_handler(MessageHandler(filters.ALL, echo))

        # Добавляем обработчик ошибок
        application.add_error_handler(error_handler)

        # Запуск бота
        application.run_polling()
    except KeyboardInterrupt:
        logger.info("Бот остановлен вручную.")
    except Exception as e:
        logger.critical("Критическая ошибка: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
