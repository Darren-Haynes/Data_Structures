"""Pytest fixures."""
import pytest


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
