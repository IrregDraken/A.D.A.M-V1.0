"""
telegram/sender.py
--------------------------------------------------
A.D.A.M V1

Handles automatic Telegram security alerts.
"""

from telegram.bot import bot
from telegram.keyboards import alert_keyboard

from config import Config


DIVIDER = "━━━━━━━━━━━━━━━━━━━━"


def send_alert(
    device_id,
    confidence,
    reason
):
    """
    Send a security alert to Telegram.
    """

    message = (

        "🚨 <b>SECURITY ALERT</b>\n\n"

        f"{DIVIDER}\n\n"

        f"📍 <b>Device</b>\n"
        f"{device_id}\n\n"

        f"⚠️ <b>Threat</b>\n"
        f"{reason}\n\n"

        f"🎯 <b>Confidence</b>\n"
        f"{confidence * 100:.0f}%\n\n"

        "🧠 <b>AI Assessment</b>\n"
        "Suspicious activity detected within a protected area.\n\n"

        f"{DIVIDER}\n\n"

        "Awaiting operator response..."
    )

    sent = bot.send_message(

        chat_id=Config.TELEGRAM_CHAT_ID,

        text=message,

        parse_mode="HTML",

        reply_markup=alert_keyboard(device_id)

    )

    return sent.message_id
