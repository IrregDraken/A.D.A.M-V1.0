"""
services/command_service.py
----------------------------------
Command Service
"""

from database import get_connection


class CommandService:

    @staticmethod
    def create_command(device_id, command):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO commands
            (device_id, command)
            VALUES (?, ?)
            """,
            (
                device_id,
                command
            )
        )

        conn.commit()

        command_id = cursor.lastrowid

        conn.close()

        return command_id

    @staticmethod
    def get_pending_command(device_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM commands
            WHERE device_id = ?
            AND status = 'pending'
            ORDER BY id ASC
            LIMIT 1
            """,
            (device_id,)
        )

        command = cursor.fetchone()

        conn.close()

        return command

    @staticmethod
    def mark_executed(command_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE commands
            SET
                status='executed',
                executed_at=CURRENT_TIMESTAMP
            WHERE id=?
            """,
            (command_id,)
        )

        conn.commit()

        conn.close()

    @staticmethod
    def get_all_commands():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM commands
            ORDER BY id DESC
            """
        )

        commands = cursor.fetchall()

        conn.close()

        return commands