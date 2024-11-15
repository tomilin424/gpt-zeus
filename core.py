import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from config import BOT_TOKEN

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

# Получаем username бота при запуске
BOT_USERNAME = bot.get_me().username

class UserStates(StatesGroup):
    waiting_for_prompt = State()
    waiting_for_image_prompt = State()
    waiting_for_claude_prompt = State()
    waiting_for_gemini_prompt = State()
    waiting_for_dalle_prompt = State()
    waiting_for_amount = State()
    waiting_for_promo = State()
    waiting_for_feedback = State()
    waiting_for_review = State()
    waiting_for_ticket_message = State()
    selecting_model = State()
    auto_renewal = State()

ADMIN_IDS = [5124939498, 241316555]

def is_admin(user_id):
    return user_id in ADMIN_IDS 