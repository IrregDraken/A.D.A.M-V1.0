"""
telegram/handlers.py
--------------------------------------------------
A.D.A.M V1

Handles every inline keyboard callback.

Responsibilities
----------------
- Navigation
- Page switching
- Alert actions
"""

from telegram.bot import bot

from telegram.views import (
    home_view,
    dashboard_view,
    about_view,
    devices_view,
    event_log_view,
    intelligence_view,
    settings_view
)

from telegram.keyboards import (
    home_keyboard,
    dashboard_keyboard,
    events_keyboard,
    devices_keyboard,
    intelligence_keyboard,
    settings_keyboard,
    about_keyboard
)

from services.command_service import CommandService


# ==================================================
# CALLBACK ROUTER
# ==================================================

@bot.callback_query_handler(func=lambda call: True)
def callback_router(call):

    data = call.data

    user = call.from_user.first_name

    chat_id = call.message.chat.id

    message_id = call.message.message_id

    # ==============================================
    # HOME
    # ==============================================

    if data == "home":

        bot.edit_message_text(

            home_view(user),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=home_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # DASHBOARD
    # ==============================================

    if data == "dashboard":

        bot.edit_message_text(

            dashboard_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=dashboard_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # EVENT LOG
    # ==============================================

    if data == "events":

        bot.edit_message_text(

            event_log_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=events_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # DEVICES
    # ==============================================

    if data == "devices":

        bot.edit_message_text(

            devices_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=devices_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # AI ENGINE
    # ==============================================

    if data == "intelligence":

        bot.edit_message_text(

            intelligence_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=intelligence_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # SETTINGS
    # ==============================================

    if data == "settings":

        bot.edit_message_text(

            settings_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=settings_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # ABOUT
    # ==============================================

    if data == "about":

        bot.edit_message_text(

            about_view(),

            chat_id,

            message_id,

            parse_mode="HTML",

            reply_markup=about_keyboard()

        )

        bot.answer_callback_query(call.id)

        return

    # ==============================================
    # ALERT ACTIONS
    # ==============================================

    if ":" in data:

        action, device_id = data.split(":")

        # ------------------------------
        # ACTIVATE ALARM
        # ------------------------------

        if action == "activate":

            CommandService.create_command(

                device_id,

                "activate_alarm"

            )

            bot.answer_callback_query(

                call.id,

                "🛡️ Alarm activation queued."

            )

            bot.edit_message_reply_markup(

                chat_id,

                message_id,

                reply_markup=None

            )

            return

        # ------------------------------
        # DISMISS ALERT
        # ------------------------------

        if action == "dismiss":

            CommandService.create_command(

                device_id,

                "dismiss"

            )

            bot.answer_callback_query(

                call.id,

                "🔕 Alert dismissed."

            )

            bot.edit_message_reply_markup(

                chat_id,

                message_id,

                reply_markup=None

            )

            return
