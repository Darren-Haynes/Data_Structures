"""Pytest fixtures."""
import pytest


@pytest.fixture
def eh():
    """Create empty BinaryHeap."""
    from binary_heap import BinaryHeap
    return BinaryHeap()
