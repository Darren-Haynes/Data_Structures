"""Pytest fixtures."""
import pytest


@pytest.fixture
def empty_q():
    """Create empty BinaryHeap."""
    from priorityq import PriorityQ
    return PriorityQ()


@pytest.fixture
def q10():
    """Create Q with 10 priorities that contain 1 value each."""
    from priorityq import PriorityQ
    q = PriorityQ()
    for i in range(1, 10):
        q.insert('a', i)
    return q
