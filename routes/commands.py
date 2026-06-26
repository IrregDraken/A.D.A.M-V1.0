"""
routes/commands.py
----------------------------------
Command API

Responsibilities:
- Deliver pending commands to ESP32.
- Mark commands as executed.
"""

from flask import Blueprint
from flask import jsonify

from services.command_service import CommandService

commands_bp = Blueprint(
    "commands",
    __name__
)


@commands_bp.route(
    "/commands/<device_id>",
    methods=["GET"]
)
def get_command(device_id):

    command = CommandService.get_pending_command(
        device_id
    )

    if command is None:

        return jsonify({
            "status": "idle"
        }), 200

    CommandService.mark_executed(
        command["id"]
    )

    return jsonify({

        "status": "success",

        "command_id": command["id"],

        "command": command["command"]

    }), 200
