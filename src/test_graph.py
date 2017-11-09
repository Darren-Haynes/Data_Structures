"""Tests for the graph, because we test all the things."""
import pytest


def test_graph_initiates_with_empty_dict(empty_g):
    """Graph initiates with an empty dict: self.graph."""
    assert empty_g.graph == {}


def test_add_node_to_empty_graph_creates_key(empty_g):
    """Add a node to empty graph creates key in graph."""
    empty_g.add_node('A')
    assert 'A' in empty_g.graph


def test_add_node_to_empty_graph_creates_value(empty_g):
    """Add a node to empty graph creates dict value as empty list."""
    empty_g.add_node('A')
    assert empty_g.graph['A'] == []


def test_add_same_node_to_graph_twice_does_nothing(empty_g):
    """If node exist, add_node() should do nothing."""
    empty_g.add_node('A')
    empty_g.add_node('A')
    assert 'A' in empty_g.graph
    assert len(empty_g.graph) == 1


def test_add_multiple_nodes_to_graph(empty_g):
    """Test 10 nodes added to graph are all in graph."""
    for i in range(10):
        empty_g.add_node(i)
    for i in range(10):
        assert i in empty_g.graph


def test_add_node_and_edge_to_node_without_edge(empty_g):
    """If node without edge exists, adding node with edge adds edge."""
    empty_g.add_node('A')
    empty_g.add_edge('A', 'B')
    assert empty_g.graph['A'] == ['B']


def test_add_node_creates_value_error(empty_g):
    """If both params passed to function are the same, raise ValueError."""
    with pytest.raises(ValueError):
        empty_g.add_edge('A', 'A')


def test_add_edge_doesnt_create_duplicate_edge(empty_g):
    """If an edge exist for node don't add it a second time."""
    empty_g.add_node('A')
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('A', 'B')
    assert empty_g.graph['A'] == ['B']


def test_all_nodes_are_returned(empty_g):
    """Test all nodes in the graph are actually returned."""
    for i in range(20):
        empty_g.add_node(i)
    assert sorted(empty_g.nodes()) == [i for i in range(20)]


def test_all_edges_returned_as_list(empty_g):
    """Test that edges() method returns all edges in graph as list."""
    from random import randint
    edges = []
    for i in range(100):
        rand_edge = randint(0, 20)
        edges.append(rand_edge)
        rand_val = rand_edge
        while rand_val == rand_edge:
            rand_val = randint(0, 20)
        empty_g.add_edge(rand_val, rand_edge)
    assert sorted(empty_g.edges()) == list(set(edges))


def test_del_node_deletes_the_node(empty_g):
    """If node in graph, node should go bye bye."""
    from random import randint
    for i in range(20):
        empty_g.add_node(i)
    rand_val = randint(0, 19)
    empty_g.del_node(rand_val)
    assert rand_val not in empty_g.graph


def test_del_node_raises_key_error(empty_g):
    """If node not in graph raise key error."""
    empty_g.add_node(1)
    with pytest.raises(KeyError):
        empty_g.del_node(0)


def test_del_edge_deletes_edge(empty_g):
    """If edge exists, delete it."""
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('A', 'C')
    empty_g.add_edge('A', 'D')
    empty_g.del_edge('A', 'B')
    assert 'B' not in empty_g.graph['A']


def test_del_edge_raises_value_error(empty_g):
    """If edge of node doesn't exist raise ValueError."""
    empty_g.add_edge('A', 'D')
    with pytest.raises(ValueError):
        empty_g.del_edge('A', 'C')


def test_del_edge_raises_key_error(empty_g):
    """If node doesn't exist raise KeyError."""
    empty_g.add_edge('A', 'D')
    with pytest.raises(KeyError):
        empty_g.del_edge('B', 'C')


def test_has_node_returns_true(empty_g):
    """If node in graph, return True."""
    empty_g.add_edge('A', 'D')
    assert empty_g.has_node('A')


def test_has_node_returns_false(empty_g):
    """If node in graph, return True."""
    empty_g.add_edge('A', 'D')
    assert not empty_g.has_node('B')


def test_neighbors_returns_key_error(empty_g):
    """If node not in graph, raise key error."""
    empty_g.add_edge('A', 'D')
    with pytest.raises(KeyError):
        empty_g.neighbors('B')


def test_neighbors_return_list_of_edges(empty_g):
    """If node exits, all its edges should be returned as list."""
    empty_g.add_node('A')
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('A', 'C')
    empty_g.add_edge('A', 'D')
    assert empty_g.neighbors('A') == ['B', 'C', 'D']


def test_adjacent_return_true_if_val1_edge_to_val2(empty_g):
    """If first param has edge with second param, return true."""
    empty_g.add_edge('A', 'B')
    assert empty_g.adjacent('A', 'B')


def test_adjacent_return_true_if_val2_edge_to_val1(empty_g):
    """If first param has edge with second param, return true."""
    empty_g.add_edge('B', 'A')
    assert empty_g.adjacent('B', 'A')


def test_adjacent_return_false_if_val1_not_edge_to_val2(empty_g):
    """If first param has edge with second param, return true."""
    empty_g.add_edge('A', 'B')
    empty_g.add_edge('B', 'C')
    assert not empty_g.adjacent('A', 'C')


def test_adjacent_return_false_if_val2_not_edge_to_val1(empty_g):
    """If first param has edge with second param, return true."""
    empty_g.add_edge('B', 'A')
    empty_g.add_edge('C', 'B')
    assert not empty_g.adjacent('C', 'A')


def test_adjacent_raise_keyerror_if_val1_not_in_graph(empty_g):
    """If val1 param not in graph, raise KeyError."""
    empty_g.add_edge('B', 'A')
    with pytest.raises(KeyError):
        empty_g.adjacent('C', 'A')


def test_adjacent_raise_keyerror_if_val2_not_in_graph(empty_g):
    """If val2 param not in graph, raise KeyError."""
    empty_g.add_edge('B', 'A')
    with pytest.raises(KeyError):
        empty_g.adjacent('A', 'C')


def test_random_ascii_char_is_returned(empty_g):
    """Test only upper case ascii chars between A-J are returned."""
    import string
    assert empty_g.random_ascii_char() in string.ascii_uppercase[:10]


def test_breadth_raises_key_error(empty_g):
    """If start node not in graph, raise KeyError."""
    empty_g.add_edge('A', 'B')
    with pytest.raises(KeyError):
        empty_g.breadth_first_traversal('C')


def test_breadth_start_node_has_no_edges(empty_g):
    """If start node has no edges, the node is returned."""
    empty_g.add_edge('A', 'B')
    empty_g.breadth_first_traversal('A') == ['A']


def test_breadth_not_get_caught_in_cycle(cyclic):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    assert cyclic.breadth_first_traversal('A') == ['A', 'B', 'C']


def test_breadth_non_cycle_returns_correct_traversal(non_ref):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    from string import ascii_uppercase as ascii_up
    assert non_ref.breadth_first_traversal('A') == list(ascii_up[:7])


def test_depth_raises_key_error(empty_g):
    """If start node not in graph, raise KeyError."""
    empty_g.add_edge('A', 'B')
    with pytest.raises(KeyError):
        empty_g.depth_first_traversal('C')


def test_depth_start_node_has_no_edges(empty_g):
    """If start node has no edges, the node is returned."""
    empty_g.add_edge('A', 'B')
    empty_g.depth_first_traversal('A') == ['A']


def test_depth_not_get_caught_in_cycle(cyclic):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    assert cyclic.depth_first_traversal('A') == ['A', 'B', 'C']


def test_depth_non_cycle_returns_correct_traversal(non_ref):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    correct_result = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert non_ref.depth_first_traversal('A') == correct_result
