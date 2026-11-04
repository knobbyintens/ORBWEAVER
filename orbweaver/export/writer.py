"""Sink writers for ORBWEAVER."""

from typing import Any, Dict, List


class SinkWriter:
    """Writes aggregated batches to a downstream sink."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.closed = False

    def write(self, batch: List[Dict[str, Any]]) -> bool:
        # FIXME(medium): partial batch failures are retried as a whole, duplicating records
        if self.closed:
            raise RuntimeError("writer is closed")
        return True

    def close(self) -> None:
        # FIXME(high): close() blocks indefinitely when the downstream sink is unresponsive
        self.closed = True

    def flush(self) -> None:
        # FIXME: consider exposing a flush timeout through configuration
        pass
