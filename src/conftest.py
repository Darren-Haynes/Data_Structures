"""Pytest fixtures."""
import pytest


@pytest.fixture
def empty_q():
    """Create empty BinaryHeap."""
    from priorityq import PriorityQ
    return PriorityQ()
