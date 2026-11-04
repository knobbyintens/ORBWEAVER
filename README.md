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

- [ ] **orbweaver/core/engine.py:22** - the bootstrap path silently drops frames when the queue is saturated
- [ ] **orbweaver/ingest/stream.py:20** - connection retries ignore broker-provided retry-after hints

## Contributing

Maintenance items are tracked inline with FIXME markers. Keep the backlog section sorted by file
path and line number. Do not edit generated release notes by hand.
