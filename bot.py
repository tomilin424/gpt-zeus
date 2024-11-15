import os
from dotenv import load_dotenv
import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, MenuButtonWebApp
import requests

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен из переменных окружения
TOKEN = os.getenv('BOT_TOKEN')

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обновляем URL на актуальный
WEBAPP_URL = "https://gpt-zeus-5tna3zfrd-vyacheslavs-projects-068c7a87.vercel.app"

def delete_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    response = requests.post(url)
    if response.status_code == 200:
        print("Webhook успешно удален!")
    else:
        print("Ошибка при удалении webhook:")
        print(response.text)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопкой для открытия веб-приложения
    keyboard = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton(
        text="Открыть GPT чат", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(webapp_button)
    
    # Устанавливаем меню с веб-приложением через прямой API запрос
    menu_url = f"https://api.telegram.org/bot{TOKEN}/setChatMenuButton"
    menu_data = {
        "chat_id": message.chat.id,
        "menu_button": {
            "type": "web_app",
            "text": "Открыть GPT чат",
            "web_app": {"url": WEBAPP_URL}
        }
    }
    requests.post(menu_url, json=menu_data)
    
    bot.reply_to(
        message, 
        "Привет! Нажми на кнопку ниже или используй меню для открытия GPT чата:",
        reply_markup=keyboard
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Доступные команды:
    /start - Открыть веб-приложение
    /help - Показать это сообщение
    
    Также вы можете использовать кнопку меню для открытия GPT чата.
    """
    bot.reply_to(message, help_text)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    keyboard = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton(
        text="Открыть GPT чат", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(webapp_button)
    
    bot.reply_to(
        message, 
        "Используйте кнопку ниже или меню для открытия GPT чата:",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    print("Удаление webhook...")
    delete_webhook()
    print("Бот запущен...")
    bot.polling(none_stop=True) 