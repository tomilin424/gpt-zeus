BOT_TOKEN = "7620633691:AAGIsVdgY-UwomIdNz9SHUmorwFkopMAEzc"
OPENAI_TOKEN = ""
MIDJOURNEY_TOKEN = ""
CLAUDE_API_KEY = ""
GEMINI_API_KEY = ""
CRYPTOBOT_TOKEN = "292846:AAQRG0902HxHb7PgyQl3Lkoh6SOfmEm3Ajm"
PROVIDER_TOKEN = ""

# Настройки цен (в копейках)
PRICES = {
    "basic": 19900,    # 199 рублей
    "pro": 49900,      # 499 рублей
    "unlimited": 99900 # 999 рублей
}

# Лимиты запросов
LIMITS = {
    "basic": {"gpt": 50, "images": 20},
    "pro": {"gpt": 200, "images": 50},
    "unlimited": {"gpt": -1, "images": -1}
}

# Настройки криптовалют для CryptoBot
ACCEPTED_CRYPTO = {
    "USDT": {
        "min_amount": 10,
        "network": "TRC20",
        "rate": 100  # 1 USDT = 100 RUB
    },
    "TON": {
        "min_amount": 10,
        "network": "TON",
        "rate": 150  # 1 TON = 150 RUB
    }
} 