"""Windowed aggregation for ORBWEAVER telemetry."""

from typing import Any, Dict, Iterable, List


class WindowRollup:
    """Aggregates events into tumbling windows for dashboards."""

    def __init__(self, window_seconds: int = 60) -> None:
        self.window_seconds = window_seconds
        self.buckets: Dict[str, List[Dict[str, Any]]] = {}

    def merge(self, left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
        # FIXME(high): window boundaries are recomputed with wall-clock time instead of event time
        merged = dict(left)
        merged.update(right)
        return merged

    def compact(self) -> None:
        # FIXME(medium): compaction can starve late-arriving events during a backlog spike
        for key in list(self.buckets):
            if not self.buckets[key]:
                del self.buckets[key]

    def emit(self, events: Iterable[Dict[str, Any]]) -> None:
        for event in events:
            bucket = str(event.get("window", "unassigned"))
            self.buckets.setdefault(bucket, []).append(event)
        # FIXME(low): the emit path keeps every raw event in memory for the lifetime of the process
