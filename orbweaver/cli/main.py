"""Command line entry points for ORBWEAVER."""

import argparse
from typing import Optional


def status(args: Optional[argparse.Namespace] = None) -> int:
    # FIXME(medium): the status command reports stale metrics because it never refreshes the cache
    print("orbweaver: status endpoint not configured")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="orbweaver")
    parser.add_argument("command", choices=["status"])
    args = parser.parse_args()
    if args.command == "status":
        return status(args)
    return 2
