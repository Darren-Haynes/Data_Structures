"""Test fixtures for the binary search tree tests."""

import pytest
from bst import Tree


@pytest.fixture
def dll_no_nodes():
    """Create empty doubly linked list."""
    from double_linked_list import DoublyLinkedList
    return DoublyLinkedList()


@pytest.fixture
def dll_three_nodes():
    """Create doubly linked list with 3 nodes."""
    from double_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('sugar glider')
    dll.push('dog')
    dll.push('cat')
    return dll


@pytest.fixture
def queue_no_nodes():
    """Create empty queue."""
    from queue import Queue
    new_queue = Queue()
    return new_queue


@pytest.fixture
def queue_three_nodes():
    """Create queue with 3 nodes."""
    from queue import Queue
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    return new_queue


@pytest.fixture
def deque_no_nodes():
    """Creat empty deque."""
    from deque import Deque
    new_deque = Deque()
    return new_deque


@pytest.fixture
def deque_append_one():
    """Create deque with one node appended."""
    from deque import Deque
    d = Deque()
    d.appendleft('a')
    return d


@pytest.fixture
def deque_append_two():
    """Create deque with 2 nodes appended."""
    from deque import Deque
    d = Deque()
    d.appendleft('a')
    d.appendleft('b')
    return d


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


@pytest.fixture
def eh():
    """Create empty BinaryHeap."""
    from binary_heap import BinaryHeap
    return BinaryHeap()


@pytest.fixture
def empty_g():
    """Create an empty graph."""
    from simple_graph import SimpleGraph
    return SimpleGraph()


@pytest.fixture
def sample_g():
    """Create an empty graph."""
    from simple_graph import SimpleGraph
    g = SimpleGraph()
    a_to_e = 'abcde'
    for char in a_to_e:
        for char2 in a_to_e:
            if char != char2:
                g.add_edge(char2, char)
    return g


@pytest.fixture
def empty_wg():
    """Create an empty graph."""
    from weighted_graph import WeightedGraph
    return WeightedGraph()


@pytest.fixture
def non_ref():
    """Create simple non referential graph."""
    from weighted_graph import WeightedGraph
    empty_wg = WeightedGraph()
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('A', 'C', 5)
    empty_wg.add_edge('B', 'D', 5)
    empty_wg.add_edge('B', 'E', 5)
    empty_wg.add_edge('C', 'F', 5)
    empty_wg.add_edge('C', 'G', 5)
    return empty_wg


@pytest.fixture
def cyclic():
    """Create simple cyclic graph."""
    from weighted_graph import WeightedGraph
    empty_wg = WeightedGraph()
    empty_wg.add_edge('A', 'B', 5)
    empty_wg.add_edge('B', 'C', 5)
    empty_wg.add_edge('C', 'A', 5)
    return empty_wg


@pytest.fixture()
def empty_t():
    """Create empty tree."""
    return Tree()


@pytest.fixture()
def one_t():
    """Create tree with one node."""
    t = Tree()
    t.insert(10)
    return t


@pytest.fixture()
def balanced_3_nodes():
    """Create balanced tree with 3 nodes."""
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    return t


@pytest.fixture()
def balanced_7_nodes():
    """Create balanced tree with 3 nodes."""
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(20)
    t.insert(13)
    t.insert(3)
    t.insert(7)
    return t
