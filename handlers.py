from bot import bot, UserStates
from telebot import types
from database import db

@bot.message_handler(func=lambda message: message.text == "🤖 GPT-4")
def gpt4_handler(message):
    bot.send_message(
        message.chat.id,
        "💬 Введите ваш запрос для GPT-4:"
    )
    bot.set_state(message.from_user.id, UserStates.waiting_for_prompt, message.chat.id)

@bot.message_handler(func=lambda message: message.text == "🎨 Midjourney")
def midjourney_handler(message):
    bot.send_message(
        message.chat.id,
        "🎨 Опишите изображение, которое хотите создать:"
    )
    bot.set_state(message.from_user.id, UserStates.waiting_for_image_prompt, message.chat.id)

@bot.message_handler(func=lambda message: message.text == "👨‍💻 Claude 3")
def claude_handler(message):
    bot.send_message(
        message.chat.id,
        "💬 Введите ваш запрос для Claude 3:"
    )
    bot.set_state(message.from_user.id, UserStates.waiting_for_claude_prompt, message.chat.id) 