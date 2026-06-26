"""
telegram/keyboards.py
--------------------------------------------------
A.D.A.M Telegram Keyboards

Contains every inline keyboard used by
the Telegram interface.
"""

from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


# ==================================================
# HOME
# ==================================================

def home_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.row(

        InlineKeyboardButton(
            "📊 Dashboard",
            callback_data="dashboard"
        ),

        InlineKeyboardButton(
            "📜 Event Log",
            callback_data="events"
        )

    )

    keyboard.row(

        InlineKeyboardButton(
            "📡 Devices",
            callback_data="devices"
        ),

        InlineKeyboardButton(
            "🧠 Intelligence",
            callback_data="intelligence"
        )

    )

    keyboard.row(

        InlineKeyboardButton(
            "⚙️ Settings",
            callback_data="settings"
        ),

        InlineKeyboardButton(
            "ℹ️ About",
            callback_data="about"
        )

    )

    return keyboard


# ==================================================
# DASHBOARD
# ==================================================

def dashboard_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.row(

        InlineKeyboardButton(
            "🔄 Refresh",
            callback_data="dashboard"
        ),

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# EVENT LOG
# ==================================================

def events_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.row(

        InlineKeyboardButton(
            "🔄 Refresh",
            callback_data="events"
        ),

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# DEVICES
# ==================================================

def devices_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.row(

        InlineKeyboardButton(
            "🔄 Refresh",
            callback_data="devices"
        ),

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# INTELLIGENCE
# ==================================================

def intelligence_keyboard():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# SETTINGS
# ==================================================

def settings_keyboard():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# ABOUT
# ==================================================

def about_keyboard():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(

        InlineKeyboardButton(
            "🏠 Home",
            callback_data="home"
        )

    )

    return keyboard


# ==================================================
# SECURITY ALERT
# ==================================================

def alert_keyboard(device_id):

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.row(

        InlineKeyboardButton(
            "🚨 Activate Alarm",
            callback_data=f"activate:{device_id}"
        ),

        InlineKeyboardButton(
            "🔕 Dismiss",
            callback_data=f"dismiss:{device_id}"
        )

    )

    keyboard.row(

        InlineKeyboardButton(
            "📊 Dashboard",
            callback_data="dashboard"
        )

    )

    return keyboard
