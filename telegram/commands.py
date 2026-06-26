"""
telegram/commands.py
--------------------------------------------------
A.D.A.M Telegram Commands

Handles Telegram slash commands.
"""

from telegram.bot import bot

from telegram.views import (
    home_view,
    about_view
)

from telegram.keyboards import (
    home_keyboard,
    about_keyboard
)


# ==================================================
# /start
# ==================================================

@bot.message_handler(commands=["start"])
def start(message):

    user = message.from_user.first_name

    bot.send_message(

        chat_id=message.chat.id,

        text=home_view(user),

        parse_mode="HTML",

        reply_markup=home_keyboard()

    )


# ==================================================
# /help
# ==================================================

@bot.message_handler(commands=["help"])
def help_command(message):

    bot.send_message(

        chat_id=message.chat.id,

        text=(

            "🛡️ <b>A.D.A.M HELP</b>\n\n"

            "Available Commands\n\n"

            "/start\n"
            "/help\n"
            "/about"

        ),

        parse_mode="HTML"

    )


# ==================================================
# /about
# ==================================================

@bot.message_handler(commands=["about"])
def about(message):

    bot.send_message(

        chat_id=message.chat.id,

        text=about_view(),

        parse_mode="HTML",

        reply_markup=about_keyboard()

    )
