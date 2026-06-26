"""
telegram/keyboards.py
"""

from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def alert_keyboard(device_id):

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(

        InlineKeyboardButton(
            "🚨 Activate Alarm",
            callback_data=f"activate:{device_id}"
        ),

        InlineKeyboardButton(
            "🔕 Ignore",
            callback_data=f"ignore:{device_id}"
        )

    )

    return keyboard
