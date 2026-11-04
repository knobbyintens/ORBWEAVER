"""Schema validation for ORBWEAVER events."""

from typing import Any, Dict, List


class EventSchema:
    """Validates event payloads against the declared schema."""

    def __init__(self, fields: List[str], strict: bool = True) -> None:
        self.fields = fields
        self.strict = strict

    def validate(self, event: Dict[str, Any]) -> bool:
        # FIXME(high): allow additional properties is enabled for every nested schema
        for field in self.fields:
            if field not in event:
                # FIXME(low): error messages leak internal field paths to callers
                return False
        return True
