# Root Cause Analysis Agent Architecture

Automated RCA agent that analyzes incidents by correlating metrics, logs, traces, and deployment events to identify the root cause of production issues, generates causal chains, and produces structured RCA reports with preventive recommendations.

## Domain Tools

- **correlate_signals**: Correlate metrics, logs, and traces around an incident window
- **analyze_traces**: Analyze distributed traces for latency bottlenecks and errors
- **find_change_correlation**: Find deployments and config changes near incident time
- **build_causal_chain**: Build causal chain from symptoms to root cause
- **generate_rca_report**: Generate structured root cause analysis report