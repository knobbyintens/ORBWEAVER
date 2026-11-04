"""Core execution engine for ORBWEAVER pipelines."""

from __future__ import annotations

import asyncio
import logging
from collections import deque
from typing import Any, Deque, Dict

logger = logging.getLogger(__name__)

DEFAULT_BUFFER_SIZE = 512


class Engine:
    """Coordinates stages of an event processing pipeline."""

    def __init__(self, buffer_size: int = DEFAULT_BUFFER_SIZE) -> None:
        self.buffer: Deque[Dict[str, Any]] = deque(maxlen=buffer_size)
        self.running = False
        self.dropped_frames = 0

    async def start(self) -> None:
        self.running = True
        logger.info("engine starting with buffer size %s", self.buffer.maxlen)

    async def stop(self) -> None:
        self.running = False
        await asyncio.sleep(0.1)

    def admit(self, frame: Dict[str, Any]) -> bool:
        if not self.running:
            raise RuntimeError("engine is not running")
        if len(self.buffer) == self.buffer.maxlen:
            self.dropped_frames += 1
            return False
        self.buffer.append(frame)
        return True

# TODO: expose queue depth through the health endpoint
