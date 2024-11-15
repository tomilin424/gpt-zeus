from core import bot
import bot as bot_handlers
import handlers

if __name__ == '__main__':
    bot_handlers.setup_commands()
    print("Zeus AI Bot запущен...")
    bot.infinity_polling() 