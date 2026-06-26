"""
routes/events.py
"""

from flask import Blueprint
from flask import jsonify
from flask import request

from ai.rules import RuleEngine

from services.event_service import EventService
from services.alert_service import AlertService


events_bp = Blueprint(
    "events",
    __name__
)


@events_bp.route(
    "/event",
    methods=["POST"]
)
def receive_event():

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "Missing JSON"
        }), 400

    device_id = data.get("device_id")
    event_type = data.get("event_type")

    if not device_id or not event_type:

        return jsonify({
            "error": "device_id and event_type required"
        }), 400

    analysis = RuleEngine.analyze(
        device_id,
        event_type
    )

    event_id = EventService.create_event(

        device_id=device_id,

        event_type=event_type,

        confidence=analysis["confidence"]

    )

    if analysis["anomaly"]:

        AlertService.create_alert(

            event_id=event_id,

            device_id=device_id,

            confidence=analysis["confidence"],

            reason=analysis["reason"]

        )

    return jsonify({

        "success": True,

        "event_id": event_id,

        "analysis": analysis

    }), 201
