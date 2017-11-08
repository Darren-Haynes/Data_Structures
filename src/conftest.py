"""Pytest Fixtures."""
import pytest


@pytest.fixture
def empty_g():
    """Create an empty graph."""
    from simple_graph import SimpleGraph
    return SimpleGraph()

