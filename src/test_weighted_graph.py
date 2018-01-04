"""Tests for the graph, because we test all the things."""
import pytest


def test_graph_initiates_with_empty_dict(empty_wg):
    """Graph initiates with an empty dict: self.graph."""
    assert empty_wg.graph == {}


def test_add_node_to_empty_wgraph_creates_key(empty_wg):
    """Add a node to empty graph creates key in graph."""
    empty_wg.add_node('A')
    assert 'A' in empty_wg.graph


def test_add_node_to_empty_wgraph_creates_value(empty_wg):
    """Add a node to empty graph creates dict value as empty list."""
    empty_wg.add_node('A')
    assert empty_wg.graph['A'] == {}


def test_add_same_node_to_graph_twice_does_nothing(empty_wg):
    """If node exist, add_node() should do nothing."""
    empty_wg.add_node('A')
    empty_wg.add_node('A')
    assert 'A' in empty_wg.graph
    assert len(empty_wg.graph) == 1


def test_add_multiple_nodes_to_graph(empty_wg):
    """Test 10 nodes added to graph are all in graph."""
    for i in range(10):
        empty_wg.add_node(i)
    for i in range(10):
        assert i in empty_wg.graph


def test_add_node_and_edge_to_node_without_edge(empty_wg):
    """If node without edge exists, adding node with edge adds edge."""
    empty_wg.add_node('A')
    empty_wg.add_edge('A', 'B', 5)
    assert empty_wg.graph['A'] == {'B': 5}


def test_add_node_creates_value_error(empty_wg):
    """If both params passed to function are the same, raise ValueError."""
    with pytest.raises(ValueError):
        empty_wg.add_edge('A', 'A', 5)

def test_add_node_errors_with_non_number_weight(empty_wg):
    """If weight not float or int valueerror should be raised."""
    with pytest.raises(ValueError):
        empty_wg.add_edge('A', 'B', '5')


def test_add_edge_int_weight_should_exist(empty_wg):
    """If weigh is int, should be added to dict."""
    empty_wg.add_edge('A', 'B', 5)
    assert empty_wg.graph['A']['B'] == 5


def test_add_edge_float_weight_should_exist(empty_wg):
    """If weigh is float, should be added to dict."""
    empty_wg.add_edge('A', 'B', 5.5)
    assert empty_wg.graph['A']['B'] == 5.5


def test_add_edge_doesnt_create_duplicate_edge(empty_wg):
    """If an edge exist for node don't add it a second time."""
    empty_wg.add_node('A')
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('A', 'B', 6)
    assert empty_wg.graph['A'] == {'B': 5}


def test_all_nodes_are_returned(empty_wg):
    """Test all nodes in the graph are actually returned."""
    for i in range(20):
        empty_wg.add_node(i)
    assert sorted(empty_wg.nodes()) == [i for i in range(20)]


def test_del_node_deletes_the_node(empty_wg):
    """If node in graph, node should go bye bye."""
    from random import randint
    for i in range(20):
        empty_wg.add_node(i)
    rand_val = randint(0, 19)
    empty_wg.del_node(rand_val)
    assert rand_val not in empty_wg.graph


def test_del_node_raises_key_error(empty_wg):
    """If node not in graph raise key error."""
    empty_wg.add_node(1)
    with pytest.raises(ValueError):
        empty_wg.del_node(0)


def test_del_edge_deletes_edge(empty_wg):
    """If edge exists, delete it."""
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('A', 'C', 5)
    empty_wg.add_edge('A', 'D', 5)
    empty_wg.del_edge('A', 'B')
    assert empty_wg.graph['A'] != {'B': 5}


def test_del_edge_raises_value_error(empty_wg):
    """If edge of node doesn't exist raise ValueError."""
    empty_wg.add_edge('A', 'D', 5)
    with pytest.raises(ValueError):
        empty_wg.del_edge('A', 'C')


def test_del_edge_raises_key_error(empty_wg):
    """If node doesn't exist raise ValueError."""
    empty_wg.add_edge('A', 'D', 5)
    with pytest.raises(ValueError):
        empty_wg.del_edge('B', 'C')


def test_has_node_returns_true(empty_wg):
    """If node in graph, return True."""
    empty_wg.add_edge('A', 'D', 5)
    assert empty_wg.has_node('A')


def test_has_node_returns_false(empty_wg):
    """If node in graph, return True."""
    empty_wg.add_edge('A', 'D', 5)
    assert not empty_wg.has_node('B')


def test_neighbors_returns_key_error(empty_wg):
    """If node not in graph, raise key error."""
    empty_wg.add_edge('A', 'D', 5)
    with pytest.raises(ValueError):
        empty_wg.neighbors('B')


def test_neighbors_return_list_of_edges(empty_wg):
    """If node exits, all its edges should be returned as list."""
    empty_wg.add_node('A')
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('A', 'C', 5)
    empty_wg.add_edge('A', 'D', 5)
    assert sorted(empty_wg.neighbors('A')) == sorted(['B', 'C', 'D'])


def test_adjacent_return_true_if_val1_edge_to_val2(empty_wg):
    """If first param has edge with second param, return true."""
    empty_wg.add_edge('A', 'B', 5)
    assert empty_wg.adjacent('A', 'B')


def test_adjacent_return_true_if_val2_edge_to_val1(empty_wg):
    """If first param has edge with second param, return true."""
    empty_wg.add_edge('B', 'A', 5)
    assert empty_wg.adjacent('B', 'A')


def test_adjacent_return_false_if_val1_not_edge_to_val2(empty_wg):
    """If first param has edge with second param, return true."""
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('B', 'C', 5)
    assert not empty_wg.adjacent('A', 'C')


def test_adjacent_return_false_if_val2_not_edge_to_val1(empty_wg):
    """If first param has edge with second param, return true."""
    empty_wg.add_edge('B', 'A', 5)
    empty_wg.add_edge('C', 'B', 5)
    assert not empty_wg.adjacent('C', 'A')


def test_adjacent_raise_keyerror_if_val1_not_in_graph(empty_wg):
    """If val1 param not in graph, raise ValueError."""
    empty_wg.add_edge('B', 'A', 5)
    with pytest.raises(ValueError):
        empty_wg.adjacent('C', 'A')


def test_adjacent_raise_keyerror_if_val2_not_in_graph(empty_wg):
    """If val2 param not in graph, raise ValueError."""
    empty_wg.add_edge('B', 'A', 5)
    with pytest.raises(ValueError):
        empty_wg.adjacent('A', 'C')


def test_random_ascii_char_is_returned(empty_wg):
    """Test only upper case ascii chars between A-J are returned."""
    import string
    assert empty_wg.random_ascii_char() in string.ascii_uppercase[:10]


def test_breadth_raises_key_error(empty_wg):
    """If start node not in graph, raise ValueError."""
    empty_wg.add_edge('A', 'B', 5)
    with pytest.raises(ValueError):
        empty_wg.breadth_first_traversal('C')


def test_breadth_start_node_has_no_edges(empty_wg):
    """If start node has no edges, the node is returned."""
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.breadth_first_traversal('A') == ['A']


def test_breadth_not_get_caught_in_cycle(cyclic):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    assert cyclic.breadth_first_traversal('A') == ['A', 'B', 'C']


def test_breadth_non_cycle_returns_correct_traversal(non_ref):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    from string import ascii_uppercase as ascii_up
    assert non_ref.breadth_first_traversal('A') == list(ascii_up[:7])


def test_depth_raises_key_error(empty_wg):
    """If start node not in graph, raise ValueError."""
    empty_wg.add_edge('A', 'B', 5)
    with pytest.raises(KeyError):
        empty_wg.depth_first_traversal('C')


def test_depth_start_node_has_no_edges(empty_wg):
    """If start node has no edges, the node is returned."""
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.depth_first_traversal('A') == ['A']


def test_depth_not_get_caught_in_cycle(cyclic):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    assert cyclic.depth_first_traversal('A') == ['A', 'B', 'C']


def test_depth_non_cycle_returns_correct_traversal(non_ref):
    """Test traversal doesn't get caught in cyclical loop in a cyclic graph."""
    correct_result = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert non_ref.depth_first_traversal('A') == correct_result


def test_edges_returns_tuple():
    """The edges method should return a tuple."""
    from weighted_graph import WeightedGraph
    g = WeightedGraph()
    g.create_random_graph()
    assert isinstance(g.edges(), tuple)
