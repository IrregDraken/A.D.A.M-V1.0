"""
services/event_service.py
----------------------------------
Event Service

Responsibilities:
- Save events to the database.
- Retrieve events when needed.

Business logic such as AI analysis or Telegram notifications
does NOT belong here.
"""

from database import get_connection


class EventService:
    """Handles database operations for sensor events."""

    @staticmethod
    def create_event(device_id, event_type, confidence, status="new"):
        """
        Save a new event to the database.

        Returns:
            int: ID of the newly created event.
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO events
            (device_id, event_type, confidence, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                device_id,
                event_type,
                confidence,
                status
            )
        )

        conn.commit()

        event_id = cursor.lastrowid

        conn.close()

        return event_id

    @staticmethod
    def get_event(event_id):
        """
        Retrieve a single event by ID.
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM events
            WHERE id = ?
            """,
            (event_id,)
        )

        event = cursor.fetchone()

        conn.close()

        return event

    @staticmethod
    def get_all_events():
        """
        Retrieve all recorded events.
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM events
            ORDER BY created_at DESC
            """
        )

        events = cursor.fetchall()

        conn.close()

        return events

