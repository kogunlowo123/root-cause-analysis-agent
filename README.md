# Root Cause Analysis Agent

[![CI](https://github.com/kogunlowo123/root-cause-analysis-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/root-cause-analysis-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated RCA agent that analyzes incidents by correlating metrics, logs, traces, and deployment events to identify the root cause of production issues, generates causal chains, and produces structured RCA reports with preventive recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `correlate_signals` | Correlate metrics, logs, and traces around an incident window |
| `analyze_traces` | Analyze distributed traces for latency bottlenecks and errors |
| `find_change_correlation` | Find deployments and config changes near incident time |
| `build_causal_chain` | Build causal chain from symptoms to root cause |
| `generate_rca_report` | Generate structured root cause analysis report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/rca/correlate` | Correlate incident signals |
| `POST` | `/api/v1/rca/traces` | Analyze distributed traces |
| `POST` | `/api/v1/rca/changes` | Find correlated changes |
| `POST` | `/api/v1/rca/causal-chain` | Build causal chain |
| `POST` | `/api/v1/rca/report` | Generate RCA report |

## Features

- Metric Correlation
- Trace Analysis
- Change Correlation
- Causal Chain
- Rca Reporting

## Integrations

- Jaeger
- Zipkin
- Prometheus
- Grafana
- Deployment Tracker

## Architecture

```
root-cause-analysis-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── root_cause_analysis_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Distributed Tracing + APM + Change Tracking**

---

Built as part of the Enterprise AI Agent Platform.
