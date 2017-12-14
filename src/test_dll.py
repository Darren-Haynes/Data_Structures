"""Test the Double Linked List."""
import pytest


def test_push_to_empty_becomes_head_tail(dll_no_nodes):
    """First node should be the tail and the head."""
    dll_no_nodes.push('a')
    assert dll_no_nodes.head.val == dll_no_nodes.tail.val == 'a'


def test_push_becomes_head(dll_three_nodes):
    """Test that every pushed node becomes the head."""
    dll_three_nodes.push(1)
    assert dll_three_nodes.head.val == 1


def test_push_and_append(dll_no_nodes):
    """Test several push and appends gives correct node as head."""
    dll_no_nodes.push(1)
    dll_no_nodes.append(2)
    dll_no_nodes.push(3)
    dll_no_nodes.append(4)
    assert(dll_no_nodes.head.val == 3)


def test_append_to_empty_becomes_head_tail(dll_no_nodes):
    """Append to empty list, new node should be head and tail."""
    dll_no_nodes.append('a')
    assert dll_no_nodes.head.val == dll_no_nodes.tail.val == 'a'


def test_append_becomes_tail(dll_three_nodes):
    """When appending, tail should be new node."""
    dll_three_nodes.append(1)
    assert dll_three_nodes.tail.val == 1


def test_pop_empty_raises_error(dll_no_nodes):
    """Pop on empty list should raise IndexError."""
    with pytest.raises(IndexError):
        dll_no_nodes.pop()


def test_pop_single_node_returns_value(dll_no_nodes):
    """Pop only node in list should return that nodes value."""
    dll_no_nodes.push('a')
    assert dll_no_nodes.pop() == 'a'


def test_pop_list_3_nodes_returns_head_value(dll_three_nodes):
    """Pop should return the head node if more than 1 node in list."""
    head_val = dll_three_nodes.head.val
    assert dll_three_nodes.pop() == head_val


def test_shift_empty_raises_error(dll_no_nodes):
    """Shift empty list should raise Index Error."""
    with pytest.raises(IndexError):
        dll_no_nodes.shift()


def test_shift_returns_tail_value(dll_three_nodes):
    """Shift should return value of the tail."""
    tail_val = dll_three_nodes.tail.val
    assert dll_three_nodes.shift() == tail_val


def test_shift_single_node_returns_nodes_value(dll_no_nodes):
    """If one node in list, shift should return that node's value."""
    dll_no_nodes.push('a')
    assert dll_no_nodes.shift() == 'a'


def test_remove_removes_from_head(dll_three_nodes):
    """Test remove, removes head if value is at the head."""
    head_val = dll_three_nodes.head.val
    dll_three_nodes.remove(head_val)
    assert dll_three_nodes.head.val != head_val


def test_remove_removes_from_tail(dll_three_nodes):
    """Remove should remove tail if tail data == to value to remove."""
    tail_val = dll_three_nodes.tail.val
    dll_three_nodes.remove(tail_val)
    assert dll_three_nodes.tail.val != tail_val


def test_remove_value_not_in_list_raises_error(dll_three_nodes):
    """Trying to remove a value not in list should raise Value Error."""
    with pytest.raises(ValueError):
        dll_three_nodes.remove('bat')


def test_len_returns_correct_value(dll_no_nodes, dll_three_nodes):
    """Test that adding nodes increments size correctly."""
    assert len(dll_no_nodes) == 0
    assert len(dll_three_nodes) == 3
    for i in range(1, 20):
        dll_no_nodes.push(i)
        assert len(dll_no_nodes) == i
