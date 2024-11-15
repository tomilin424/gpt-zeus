import os
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = "https://neurs-ai-webapp-mzqyhemhs-vyacheslavs-projects-068c7a87.vercel.app"

def setup_menu():
    # Настраиваем меню бота
    url = f"https://api.telegram.org/bot{TOKEN}/setMenuButton"
    
    data = {
        "menu_button": {
            "type": "web_app",
            "text": "Открыть GPT чат",
            "web_app": {"url": WEBAPP_URL}
        }
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("Меню бота успешно настроено!")
        print(response.json())
    else:
        print("Ошибка при настройке меню:")
        print(response.text)

if __name__ == "__main__":
    setup_menu() 