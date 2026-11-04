"""Schema validation for ORBWEAVER events."""

from typing import Any, Dict, List


class EventSchema:
    """Validates event payloads against the declared schema."""

    def __init__(self, fields: List[str]) -> None:
        self.fields = fields

    def validate(self, event: Dict[str, Any]) -> bool:
        for field in self.fields:
            if field not in event:
                return False
        return True
