import os
from dotenv import load_dotenv
import requests

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# URL вашего веб-приложения
WEBAPP_URL = "https://neurs-ai-webapp-mzqyhemhs-vyacheslavs-projects-068c7a87.vercel.app"

def update_bot_settings():
    # API endpoint для обновления настроек бота
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    
    # Параметры для обновления
    params = {
        "url": WEBAPP_URL,
        "allowed_updates": ["message", "callback_query"]
    }
    
    # Отправляем запрос
    response = requests.post(url, json=params)
    
    if response.status_code == 200:
        print("URL веб-приложения успешно обновлен!")
        print(response.json())
    else:
        print("Ошибка при обновлении URL:")
        print(response.text)

if __name__ == "__main__":
    update_bot_settings() 