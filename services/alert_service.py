"""
services/alert_service.py
----------------------------------
Alert Service

Responsibilities
----------------
- Prevent duplicate alerts
- Send Telegram alerts
- Store alert records
"""

from database import get_connection
from telegram.sender import send_alert


class AlertService:

    @staticmethod
    def alert_exists(event_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM alerts
            WHERE event_id=?
            """,
            (event_id,)
        )

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    @staticmethod
    def create_alert(
        event_id,
        device_id,
        confidence,
        reason
    ):

        if AlertService.alert_exists(event_id):
            return

        message_id = send_alert(
            device_id=device_id,
            confidence=confidence,
            reason=reason
        )

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO alerts
            (
                event_id,
                telegram_message_id,
                alert_status
            )
            VALUES
            (
                ?,
                ?,
                'sent'
            )
            """,
            (
                event_id,
                message_id
            )
        )

        conn.commit()
        conn.close()
