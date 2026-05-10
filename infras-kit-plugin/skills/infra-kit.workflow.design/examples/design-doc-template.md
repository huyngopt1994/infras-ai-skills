# Infrastructure Design Doc

## Summary

<BLUF: what is being built/changed and the intended outcome>

## Problem

- Current state:
- Pain/risks:
- Why now:

## Goals And Non-Goals

- Goals:
- Non-goals:

## Requirements

- Functional:
- Non-functional (SLOs, RTO/RPO, compliance):

## Current Architecture

<Short description. Link to diagrams if they exist.>

## Diagrams

### System Diagram

```mermaid
flowchart LR
  %% Components, dependencies, and trust boundaries
  %% Replace placeholders with real components.
  User[User/Client]
  subgraph TrustBoundary[Trust boundary]
    App[Service / App]
    Data[(Data store)]
  end
  Ext[External dependency]

  User --> App
  App --> Data
  App --> Ext
```

### Flow Diagram

```mermaid
sequenceDiagram
  %% Primary flow plus one failure/degraded path.
  participant C as Client
  participant S as Service
  participant D as Dependency

  C->>S: Request
  S->>D: Call dependency
  alt Success
    D-->>S: 200 OK
    S-->>C: 200 OK
  else Failure (example)
    D-->>S: 5xx / timeout
    S-->>C: 503 + retry-after (or degraded response)
  end
```

## Proposed Design

- Components:
- Data flow:
- Dependency map:

## Options Considered

1. Option A:
2. Option B:

## Trade-offs

- Reliability:
- Security:
- Operational complexity:
- Cost:

## Rollout Plan

- Stages:
- Verification:
- Rollback criteria:
- Rollback steps:

## Observability

- SLIs and dashboards:
- Alerts:
- Runbooks:

## Security

- IAM:
- Network boundaries:
- Secrets:
- Audit:

## Open Questions

-
