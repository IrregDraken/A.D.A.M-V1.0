"""
config.py
----------------------------------
Central configuration for A.D.A.M V1.

Every configurable value in the application should be defined here.
This keeps the project clean and avoids hardcoding values throughout
the codebase.
"""

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    """Application configuration."""

    # ==========================================================
    # Flask Settings
    # ==========================================================

    # Secret key used by Flask for sessions and security.
    SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret")

    # True during development, False in production.
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Server configuration.
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))

    # ==========================================================
    # Database
    # ==========================================================

    # SQLite database location.
    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "instance/adam.db"
    )

    # ==========================================================
    # Telegram
    # ==========================================================

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # ==========================================================
    # AI Rule Engine
    # ==========================================================

    # Minimum confidence required before an alert is generated.
    ANOMALY_THRESHOLD = 0.90

    # ==========================================================
    # Device Settings
    # ==========================================================

    # ESP32 polling interval (seconds)
    COMMAND_POLL_INTERVAL = 3

    # Allowed event types.
    VALID_EVENT_TYPES = [
        "motion"
    ]