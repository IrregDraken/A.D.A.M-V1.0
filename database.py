"""
database.py
----------------------------------
Database manager for A.D.A.M V1.

Responsibilities:
- Create SQLite database.
- Create required tables.
- Provide database connections.

Nothing else should directly manage database creation.
"""

import os
import sqlite3

from config import Config


def get_connection():
    """
    Returns a new SQLite connection.
    """

    # Ensure the instance folder exists
    os.makedirs(os.path.dirname(Config.DATABASE_PATH), exist_ok=True)

    connection = sqlite3.connect(Config.DATABASE_PATH)

    # Return rows like dictionaries
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Creates all required tables if they do not exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================================================
    # Events Table
    # ==========================================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            confidence REAL NOT NULL,
            status TEXT DEFAULT 'new',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ==========================================================
    # Alerts Table
    # ==========================================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            telegram_message_id TEXT,
            alert_status TEXT DEFAULT 'sent',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(event_id) REFERENCES events(id)
        )
    """)

    # ==========================================================
    # Commands Table
    # ==========================================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            command TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            executed_at TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("✅ Database initialized successfully.")