# Telegram Bot

Этот бот отвечает на любое полученное сообщение, отправляя информацию об ID пользователя, ID группы/чата и ID темы (если применимо).

## Возможности
- Отправляет в ответ ID пользователя, группы/чата и темы сообщения.
- Обработывает все входящие сообщения.
- Устойчив к ошибкам, продолжает работать без перебоев.

---

## Требования
- Python 3.8 или выше
- Установленный `pip`
- Рабочий токен Telegram-бота от [BotFather](https://core.telegram.org/bots#botfather)

---

## Установка и запуск

### 1. Клонирование репозитория
Склонируйте репозиторий на ваш сервер:
```bash
git clone <URL вашего репозитория>
cd <папка проекта>
```

### 2. Создание виртуального окружения
Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

### 4. Указание токена
Откройте файл bot.py и измените токен на свой
```bash
nano bot.py
```

### 5. Запуск бота в Screen
Используйте screen для запуска бота, чтобы он продолжал работать в фоне:
```bash
screen -S message_thread_id_bot
python bot.py
```

Чтобы выйти из сессии screen, не останавливая бота, нажмите Ctrl+A, затем D.
Для возвращения в сессию выполните:
```bash
screen -r message_thread_id_bot
```

### 6. Остановка бота
Для остановки процесса бота подключитесь к сессии screen и нажите Ctrl+C или Ctrl+Z

### Примечания
Бот был протестирован на Debian GNU/Linux 12.
Используется библиотека python-telegram-bot==20.3.
Для отладки включено логирование.
Возможно нужно добавить в @BotFather для вашего бота любую команду, например /test, а также дать разрешения на добавления в группы с правом публикации.
