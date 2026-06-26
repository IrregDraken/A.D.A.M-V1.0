"""
routes/__init__.py
"""

from .events import events_bp
from .commands import commands_bp


def register_blueprints(app):

    app.register_blueprint(events_bp)

    app.register_blueprint(commands_bp)