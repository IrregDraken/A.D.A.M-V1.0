"""
telegram/sender.py
"""

from telegram.bot import bot
from telegram.keyboards import alert_keyboard

from config import Config


def send_alert(
    device_id,
    confidence,
    reason
):

    message = (
        "🚨 <b>A.D.A.M SECURITY ALERT</b>\n\n"

        f"Device : <b>{device_id}</b>\n"

        f"Reason : <b>{reason}</b>\n"

        f"Confidence : <b>{confidence:.2f}</b>"
    )

    sent = bot.send_message(

        Config.TELEGRAM_CHAT_ID,

        message,

        reply_markup=alert_keyboard(device_id)

    )

    return sent.message_id
