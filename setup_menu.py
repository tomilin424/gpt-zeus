import os
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = "https://gpt-zeus.vercel.app"

def setup_menu():
    # Используем правильный метод API
    url = f"https://api.telegram.org/bot{TOKEN}/setChatMenuButton"
    
    data = {
        "menu_button": {
            "type": "web_app",
            "text": "Открыть GPT чат",
            "web_app": {"url": WEBAPP_URL}
        }
    }
    
    # Добавляем headers
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Меню бота успешно настроено!")
        print(response.json())
    else:
        print("Ошибка при настройке меню:")
        print(response.text)
        print(f"Статус код: {response.status_code}")

if __name__ == "__main__":
    setup_menu() 