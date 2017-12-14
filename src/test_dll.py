import pytest


def test_push_to_empty_becomes_head_tail(dll_no_nodes):
    dll_no_nodes.push('a')
    assert dll_no_nodes.head.val == dll_no_nodes.tail.val == 'a'


def test_push_becomes_head(dll_three_nodes):
    dll_three_nodes.push(1)
    assert dll_three_nodes.head.val == 1


def test_push_and_append(dll_no_nodes):
    dll_no_nodes.push(1)
    dll_no_nodes.append(2)
    dll_no_nodes.push(3)
    dll_no_nodes.append(4)
    assert(dll_no_nodes.head.val == 3)


def test_append_to_empty_becomes_head_tail(dll_no_nodes):
    dll_no_nodes.append('a')
    assert dll_no_nodes.head.val == dll_no_nodes.tail.val == 'a'


def test_append_becomes_tail(dll_three_nodes):
    dll_three_nodes.append(1)
    assert dll_three_nodes.tail.val == 1


def test_pop_empty_raises_error(dll_no_nodes):
    with pytest.raises(IndexError):
        dll_no_nodes.pop()


def test_pop_returns_head_value(dll_three_nodes):
    head_val = dll_three_nodes.head.val
    assert dll_three_nodes.pop() == head_val


def test_shift_empty_raises_error(dll_no_nodes):
    with pytest.raises(IndexError):
        dll_no_nodes.shift()


def test_shift_returns_tail_value(dll_three_nodes):
    tail_val = dll_three_nodes.tail.val
    assert dll_three_nodes.shift() == tail_val


def test_remove_removes_from_head(dll_three_nodes):
    head_val = dll_three_nodes.head.val
    dll_three_nodes.remove(head_val)
    assert dll_three_nodes.head.val != head_val


def test_remove_removes_from_tail(dll_three_nodes):
    tail_val = dll_three_nodes.tail.val
    dll_three_nodes.remove(tail_val)
    assert dll_three_nodes.tail.val != tail_val


def test_remove_value_not_in_list_raises_error(dll_three_nodes):
    with pytest.raises(ValueError):
        dll_three_nodes.remove('bat')


def test_len_returns_correct_value(dll_no_nodes, dll_three_nodes):
    assert len(dll_no_nodes) == 0
    assert len(dll_three_nodes) == 3
    for i in range(1, 20):
        dll_no_nodes.push(i)
        assert len(dll_no_nodes) == i
