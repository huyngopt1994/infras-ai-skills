# 🚨 K8s Incident Triage Agent

> AI-powered incident analysis for Kubernetes using logs, metrics, and cluster state.

---

## 🔥 What is this?

K8s Incident Triage Agent analyzes production issues by correlating:

- 📜 Logs  
- 📊 Metrics  
- ⚙️ Kubernetes state  
- 🚨 Alerts  

…and returns:

- 🧠 Likely root cause  
- 📊 Supporting evidence  
- ⏱ Timeline of events  
- 🔍 Next debugging steps  
- 🛠 Suggested remediation  

---

## 🚀 Demo

### Command

```bash
obs-agent analyze checkout-api \
  --namespace payments \
  --since 10m
```

### Output

```
🚨 Incident Summary
checkout-api latency spike detected (10:31–10:38)

🧠 Likely Cause (confidence: 0.82)
Database connection saturation

📊 Evidence
- p99 latency increased 4x
- 5xx error rate increased from 0.2% → 8.1%
- DB timeout errors appeared at 10:30:42
- CPU/memory remained stable

⏱ Timeline
10:28 rollout started
10:30 DB timeout logs begin
10:31 latency spike
10:32 error rate spike

🔍 Next Checks
- kubectl describe deploy checkout-api -n payments
- check DB connection pool metrics
- verify recent config change

🛠 Suggested Fix
- increase DB pool OR rollback deployment
```

---

## 🏗 Architecture

```
User / CLI / Slack
        ↓
Incident Orchestrator
        ↓
Logs + Metrics + K8s State + Alerts
        ↓
Context Normalizer
        ↓
Correlation Engine
        ↓
LLM (Claude / GPT)
        ↓
Structured Incident Report
```

---

## 🧱 Design Blueprint

- **Incident Orchestrator**: entrypoint that authenticates to the cluster, resolves the target namespace/service, and fans out evidence collection tasks with deadlines.
- **Collector Pack**: pluggable adapters (Prometheus, Loki, CloudWatch, kubectl snapshotter) that emit raw observations in a shared protobuf/JSON schema (`kind`, `source`, `timestamp`, `body`).
- **Context Normalizer**: deduplicates snippets, extracts entities (deployments, pods, alerts) and fills a rolling timeline window so downstream models always receive aligned metrics/logs/state.
- **Correlation Engine**: rules + lightweight scoring models that compute confidence per hypothesis; produces ranked suspects with linked evidence IDs.
- **LLM Presenter**: converts the correlation bundle into human output (summary + evidence table + timeline + next actions) and enforces a response schema for CLI/UI consumption.
- **Storage / Cache**: optional sqlite/redis layer that tracks past incidents for regression detection or triaging repeated failures.

Key data contracts:

```json
{
  "id": "evt-123",
  "kind": "metric",
  "source": "prometheus",
  "scope": {
    "service": "checkout-api",
    "namespace": "payments"
  },
  "timestamps": {
    "observed": "2024-04-01T10:31:00Z"
  },
  "body": {
    "metric": "http_server_latency_p99",
    "value": 1200,
    "unit": "ms"
  }
}
```

---

## 🛠 Implementation Plan

1. **Bootstrap CLI skeleton** using Cobra/urfave (Go) or Typer (Python); wire `obs-agent analyze` command with flag parsing + config loading.
2. **Add Kubernetes session manager** that reuses contexts, enforces read-only verbs, and collects pod/deployment state snapshots.
3. **Implement collector adapters** starting with Prometheus (metrics) and Loki (logs); define adapter interface + mock implementations for tests.
4. **Ship context normalizer service** that merges metrics/logs/state into a timeline and tags anomalies with statistical z-scores.
5. **Build correlation engine** containing heuristic rules (e.g., rollout overlap, pod restarts, saturation) and a lightweight scoring model persisted under `processors/`.
6. **Integrate LLM presenter** via OpenAI/Anthropic SDKs; enforce JSON schema output and add redaction guards before sending telemetry.
7. **Deliver CLI UX** that renders tables, highlights confidence score, and prints follow-up kubectl commands; expose `--explain` to show raw evidence IDs.
8. **Add regression tests + fixtures** inside `examples/` to keep snapshot outputs stable while iterating on scoring rules.

For the very first sprint, focus on steps 1–3 to get an end-to-end thin slice (CLI → collectors → stubbed report) before layering on correlation/LLM sophistication.

---

## ⚙️ Usage

```bash
obs-agent analyze <service> \
  --namespace <ns> \
  --since 10m
```

---

## 🧪 Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
obs-agent analyze checkout-api --namespace payments --since 10m --explain
```

- `--since`: lookback window (`5m`, `2h`, `1d`)
- `--explain`: prints the ranked hypotheses + evidence matrix
- Output includes summary, likely cause, supporting evidence, timeline rows, and suggested next kubectl/prometheus checks.

---

## 📁 Project Structure

```
obs-agent/
├── cmd/
├── collectors/
├── processors/
├── llm/
├── schemas/
├── examples/
└── README.md
```

---

## 🧭 Roadmap

- v1: CLI + basic correlation
- v2: Prometheus + Loki integration
- v3: Slack + alert integration
- v4: learning + automation

---

## ⭐ If this helps

Give it a star 🚀
