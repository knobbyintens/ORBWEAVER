"""Unit tests for the ORBWEAVER engine."""

import asyncio

from orbweaver.core.engine import Engine


def test_engine_admits_frames() -> None:
    # FIXME(high): flaky test waits on a hard-coded sleep instead of the engine event
    engine = Engine(buffer_size=4)
    asyncio.run(engine.start())
    assert engine.admit({"id": 1}) is True
