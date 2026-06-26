"""
telegram/bot.py
------------------------------------
Creates the Telegram bot instance.

Responsibilities:
- Initialize the bot.
- Provide a single shared bot object.

Nothing else belongs here.
"""

import telebot

from config import Config


# Ensure the bot token exists
if not Config.TELEGRAM_BOT_TOKEN:
    raise RuntimeError(
        "TELEGRAM_BOT_TOKEN not found. Check your .env file."
    )


# Create ONE bot instance for the whole project
bot = telebot.TeleBot(
    Config.TELEGRAM_BOT_TOKEN,
    parse_mode="HTML"
)