import os
from dotenv import load_dotenv
import requests

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

def delete_webhook():
    # API endpoint для удаления webhook
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    
    # Отправляем запрос
    response = requests.post(url)
    
    if response.status_code == 200:
        print("Webhook успешно удален!")
        print(response.json())
    else:
        print("Ошибка при удалении webhook:")
        print(response.text)

if __name__ == "__main__":
    delete_webhook() 