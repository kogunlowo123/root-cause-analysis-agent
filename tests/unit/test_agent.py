"""Root Cause Analysis Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_correlate_signals():
    """Test Correlate metrics, logs, and traces around an incident window."""
    tools = AgentTools()
    result = await tools.correlate_signals(incident_time="test", window_minutes=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_traces():
    """Test Analyze distributed traces for latency bottlenecks and errors."""
    tools = AgentTools()
    result = await tools.analyze_traces(trace_ids="test", service="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_find_change_correlation():
    """Test Find deployments and config changes near incident time."""
    tools = AgentTools()
    result = await tools.find_change_correlation(time_range="test", environments="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_build_causal_chain():
    """Test Build causal chain from symptoms to root cause."""
    tools = AgentTools()
    result = await tools.build_causal_chain(symptoms="test", evidence="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.root_cause_analysis_agent_agent import RootCauseAnalysisAgentAgent
    agent = RootCauseAnalysisAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
