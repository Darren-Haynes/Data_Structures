"""Pytest Fixtures."""
import pytest


@pytest.fixture
def empty_g():
    """Create an empty graph."""
    from simple_graph import SimpleGraph
    return SimpleGraph()


@pytest.fixture
def non_ref():
    """Create simple non referential graph."""
    from simple_graph import SimpleGraph
    empty_g = SimpleGraph()
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('A', 'C')
    empty_g.add_edge('B', 'D')
    empty_g.add_edge('B', 'E')
    empty_g.add_edge('C', 'F')
    empty_g.add_edge('C', 'G')
    return empty_g


@pytest.fixture
def cyclic():
    """Create simple cyclic graph."""
    from simple_graph import SimpleGraph
    empty_g = SimpleGraph()
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('B', 'C')
    empty_g.add_edge('C', 'A')
    return empty_g
