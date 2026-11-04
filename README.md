# ORBWEAVER

ORBWEAVER is an event-stream observability toolkit for high-throughput telemetry pipelines. It
coordinates broker ingestion, event validation and windowed aggregation for internal dashboards.

## Overview

The toolkit is split into a small core engine, an ingest layer and (on the release line) analytics
and export packages. The release line is cut from main once the engine hardening work is complete.

## Getting Started

```bash
pip install -e .
orbweaver status
```

## Repository Layout

```
orbweaver/
  core/        execution engine
  ingest/      broker readers and schema validation
  analytics/   windowed rollups
  export/      sink writers
  cli/         command line entry points
```

## 🧭 Maintenance Backlog

- [ ] **orbweaver/analytics/rollup.py:14** - window boundaries are recomputed with wall-clock time instead of event time
- [ ] **orbweaver/analytics/rollup.py:20** - compaction can starve late-arriving events during a backlog spike
- [ ] **orbweaver/cli/main.py:8** - the status command reports stale metrics because it never refreshes the cache
- [ ] **orbweaver/core/engine.py:22** - the bootstrap path silently drops frames when the queue is saturated
- [ ] **orbweaver/core/engine.py:30** - shutdown does not flush the in-flight buffer before closing sockets
- [ ] **orbweaver/core/engine.py:41** - backpressure is reported only through a counter, no health signal is emitted
- [ ] **orbweaver/export/writer.py:14** - partial batch failures are retried as a whole, duplicating records
- [ ] **orbweaver/export/writer.py:20** - close() blocks indefinitely when the downstream sink is unresponsive
- [ ] **orbweaver/ingest/schema.py:14** - allow additional properties is enabled for every nested schema
- [ ] **orbweaver/ingest/stream.py:20** - connection retries ignore broker-provided retry-after hints
- [ ] **orbweaver/ingest/stream.py:27** - a dropped broker connection in the middle of a batch loses the checkpoint
- [ ] **orbweaver/ingest/stream.py:33** - checkpoints are written without a durable fsync before acknowledging

## Contributing

Maintenance items are tracked inline with FIXME markers. Keep the backlog section sorted by file
path and line number. Do not edit generated release notes by hand.
