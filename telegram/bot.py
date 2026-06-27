"""
telegram/bot.py
------------------------------------
Creates the shared Telegram bot instance.
"""

import telebot

from config import Config


TOKEN = Config.TELEGRAM_BOT_TOKEN

if not TOKEN:

    raise RuntimeError(
        "\n"
        "TELEGRAM_BOT_TOKEN is missing.\n\n"
        "Local:\n"
        "  Add it to your .env file.\n\n"
        "Production:\n"
        "  Add it as a Fly Secret:\n"
        "  fly secrets set TELEGRAM_BOT_TOKEN=<token>\n"
    )


bot = telebot.TeleBot(
    TOKEN,
    parse_mode="HTML"
)
