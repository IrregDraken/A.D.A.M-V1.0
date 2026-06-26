"""
app.py
----------------------------------
Main entry point for A.D.A.M V1

Responsibilities
----------------
- Create the Flask application
- Load configuration
- Initialize the database
- Register API routes
- Start Telegram polling
- Start the Flask server
"""

from threading import Thread

from flask import Flask

from config import Config
from database import initialize_database
from routes import register_blueprints

# Importing from telegram automatically registers handlers
from telegram import bot


def start_telegram():
    """
    Starts Telegram polling in a background thread.
    """

    print("[A.D.A.M] Telegram polling started...")

    bot.infinity_polling(
        skip_pending=True,
        timeout=30,
        long_polling_timeout=30
    )


def create_app():
    """
    Flask Application Factory.
    """

    app = Flask(__name__)

    # Load configuration
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # Initialize database
    initialize_database()

    # Register all routes
    register_blueprints(app)

    # Health Check
    @app.route("/")
    def home():
        return {
            "project": "A.D.A.M V1",
            "status": "running",
            "version": "1.0"
        }

    return app


# -------------------------------------------------
# Create Flask App
# -------------------------------------------------

app = create_app()


# -------------------------------------------------
# Start Telegram Polling Thread
# -------------------------------------------------

telegram_thread = Thread(
    target=start_telegram,
    daemon=True
)

telegram_thread.start()


# -------------------------------------------------
# Run Flask
# -------------------------------------------------

if __name__ == "__main__":

    print("[A.D.A.M] Flask server starting...")

    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG,
        use_reloader=False
    )
