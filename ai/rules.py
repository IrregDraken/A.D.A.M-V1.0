"""
ai/rules.py
----------------------------------
Rule-Based AI Engine for A.D.A.M V1

Responsibilities:
- Analyze incoming sensor events.
- Decide whether an event is anomalous.
- Return a standardized analysis result.

This MVP uses deterministic rules instead of machine learning.
"""

from config import Config


class RuleEngine:
    """Simple rule-based anomaly detector."""

    @staticmethod
    def analyze(device_id: str, event_type: str) -> dict:
        """
        Analyze an incoming event.

        Args:
            device_id (str): Unique device identifier.
            event_type (str): Type of event received.

        Returns:
            dict: Analysis result.
        """

        # Reject unsupported event types.
        if event_type not in Config.VALID_EVENT_TYPES:
            return {
                "anomaly": False,
                "confidence": 0.0,
                "reason": "Unsupported event type"
            }

        # MVP Rule:
        # Every valid motion event is considered suspicious.
        if event_type == "motion":
            return {
                "anomaly": True,
                "confidence": 0.95,
                "reason": "Motion detected"
            }

        # Fallback.
        return {
            "anomaly": False,
            "confidence": 0.0,
            "reason": "No rule matched"
        }

