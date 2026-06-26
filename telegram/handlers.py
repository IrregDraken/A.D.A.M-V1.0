"""
telegram/handlers.py
"""

from telegram.bot import bot

from services.command_service import (
    CommandService
)
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    action, device_id = call.data.split(":")

    if action == "activate":

        CommandService.create_command(
            device_id,
            "activate_alarm"
        )

        text = "✅ Alarm activation queued."

    elif action == "ignore":

        CommandService.create_command(
            device_id,
            "ignore"
        )

        text = "✅ Event ignored."

    else:

        text = "Unknown action."

    bot.answer_callback_query(
        call.id,
        text
    )

    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )