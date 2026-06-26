"""
services/dashboard_service.py
--------------------------------------------------
A.D.A.M V1 Dashboard Service

Responsibilities
----------------
- Dashboard statistics
- Home statistics
- Event history
- Device information
- Pending command count

This service NEVER talks to Telegram.
It ONLY retrieves information from SQLite.
"""

from database import get_connection


class DashboardService:

    # ==================================================
    # DASHBOARD STATS
    # ==================================================

    @staticmethod
    def get_stats():

        conn = get_connection()
        cursor = conn.cursor()

        # -------------------------
        # Total Events
        # -------------------------

        cursor.execute(
            "SELECT COUNT(*) AS total FROM events"
        )

        total_events = cursor.fetchone()["total"]

        # -------------------------
        # Total Alerts
        # -------------------------

        cursor.execute(
            "SELECT COUNT(*) AS total FROM alerts"
        )

        total_alerts = cursor.fetchone()["total"]

        # -------------------------
        # Pending Commands
        # -------------------------

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM commands
            WHERE status='pending'
        """)

        pending = cursor.fetchone()["total"]

        # -------------------------
        # Connected Devices
        # -------------------------

        cursor.execute("""
            SELECT COUNT(DISTINCT device_id) AS total
            FROM events
        """)

        devices = cursor.fetchone()["total"]

        # -------------------------
        # Latest Event
        # -------------------------

        cursor.execute("""
            SELECT
                device_id,
                event_type,
                created_at
            FROM events
            ORDER BY id DESC
            LIMIT 1
        """)

        latest = cursor.fetchone()

        conn.close()

        return {

            "devices": devices,

            "events": total_events,

            "alerts": total_alerts,

            "pending": pending,

            "last_event": latest

        }

    # ==================================================
    # RECENT EVENTS
    # ==================================================

    @staticmethod
    def get_recent_events(limit=10):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                device_id,
                event_type,
                created_at
            FROM events
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        events = cursor.fetchall()

        conn.close()

        return events

    # ==================================================
    # CONNECTED DEVICES
    # ==================================================

    @staticmethod
    def get_devices():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                device_id,

                MAX(created_at) AS last_seen,

                COUNT(*) AS total_events

            FROM events

            GROUP BY device_id

            ORDER BY device_id
        """)

        devices = cursor.fetchall()

        conn.close()

        return devices

    # ==================================================
    # SYSTEM HEALTH
    # ==================================================

    @staticmethod
    def system_health():

        stats = DashboardService.get_stats()

        if stats["pending"] > 20:

            return "🔴 Critical"

        if stats["alerts"] > 10:

            return "🟡 Warning"

        return "🟢 Nominal"
