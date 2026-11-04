"""Example pipeline wiring for local experiments."""

from orbweaver.core.engine import Engine
from orbweaver.ingest.stream import StreamReader

# FIXME(medium): demo keeps a global connection open after the script exits
ENGINE = Engine()
READER = StreamReader("memory://local-demo")


def run() -> None:
    print("demo pipeline configured")
