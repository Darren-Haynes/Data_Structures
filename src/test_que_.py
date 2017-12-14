"""Test the queue."""
import pytest


def test_enqueue_adds_to_front_and_back_on_empty(queue_no_nodes):
    queue_no_nodes.enqueue('a')
    assert queue_no_nodes.front.value == 'a'
    assert queue_no_nodes.back.value == 'a'


def test_last_enqueue_is_back(queue_no_nodes):
    queue_no_nodes.enqueue('a')
    queue_no_nodes.enqueue('b')
    queue_no_nodes.enqueue('c')
    queue_no_nodes.enqueue('d')
    assert queue_no_nodes.back.value == 'd'


def test_dequeue_changes_front_node(queue_three_nodes):
    old_value = queue_three_nodes.peek()
    queue_three_nodes.dequeue()
    assert old_value is not queue_three_nodes.peek()


def test_dequeue_last_node_empties_front_and_back(queue_three_nodes):
    queue_three_nodes.dequeue()
    queue_three_nodes.dequeue()
    queue_three_nodes.dequeue()
    assert queue_three_nodes.front is None
    assert queue_three_nodes.back is None


def test_dequeue_on_empty_raises_error(queue_no_nodes):
    with pytest.raises(IndexError):
        queue_no_nodes.dequeue()


def test_enqueue_changes_size(queue_no_nodes):
    for i in range(1, 100000):
        queue_no_nodes.enqueue(i)
        assert queue_no_nodes.size() == i


def test_peek_at_empty_returns_none(queue_no_nodes):
    assert queue_no_nodes.peek() is None


def test_len_works(queue_three_nodes):
    assert len(queue_three_nodes) == 3


def test_values_passed_through_retain_order(queue_no_nodes):
    start = [2, 'blerg', 4.6, 'rugrogreg', 0]
    for i in range(len(start)):
        queue_no_nodes.enqueue(start[i])

    end = []

    while queue_no_nodes.size():
        end.append(queue_no_nodes.dequeue())

    assert start == end
