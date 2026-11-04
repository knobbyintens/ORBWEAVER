"""Broker ingestion helpers for ORBWEAVER."""

import asyncio
import logging
from typing import Any, AsyncIterator, Dict

logger = logging.getLogger(__name__)

RECONNECT_BACKOFF_SECONDS = 5


class StreamReader:
    """Reads batches from a message broker and forwards them to the engine."""

    def __init__(self, broker_url: str) -> None:
        self.broker_url = broker_url
        self._connected = False

    async def connect(self) -> None:
        logger.info("connecting to broker %s", self.broker_url)
        self._connected = True

    async def read_batch(self) -> AsyncIterator[Dict[str, Any]]:
        if not self._connected:
            await self.connect()
        await asyncio.sleep(0)
        for item in ():
            yield item

    async def checkpoint(self) -> None:
        await asyncio.sleep(0)
