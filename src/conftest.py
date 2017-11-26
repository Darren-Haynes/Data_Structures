"""Pytest Fixtures."""
import pytest


@pytest.fixture
def empty_g():
    """Create an empty graph."""
    from weighted_graph import WeightedGraph
    return WeightedGraph()


@pytest.fixture
def non_ref():
    """Create simple non referential graph."""
    from weighted_graph import WeightedGraph
    empty_g = WeightedGraph()
    empty_g.add_edge('A', 'B', 5)
    empty_g.add_edge('A', 'C', 5)
    empty_g.add_edge('B', 'D', 5)
    empty_g.add_edge('B', 'E', 5)
    empty_g.add_edge('C', 'F', 5)
    empty_g.add_edge('C', 'G', 5)
    return empty_g


@pytest.fixture
def cyclic():
    """Create simple cyclic graph."""
    from weighted_graph import WeightedGraph
    empty_g = WeightedGraph()
    empty_g.add_edge('A', 'B', 5)
    empty_g.add_edge('B', 'C', 5)
    empty_g.add_edge('C', 'A', 5)
    return empty_g
