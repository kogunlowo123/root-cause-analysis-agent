"""Test configuration for Root Cause Analysis Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "root-cause-analysis-agent", "category": "DevOps & Platform Engineering"}
