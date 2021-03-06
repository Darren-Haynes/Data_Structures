"""Tests for the linked list."""

import pytest


def test_node_has_attributes():
    """A node object must have a.value and next attribute."""
    from linked_list import Node
    n = Node(1)
    assert hasattr(n, 'value')
    assert hasattr(n, 'next_node')


def test_linked_list_had_head():
    """A new linked list should have a head."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """Linded List push method should add a new item to the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.value == 'val'


def test_linked_list_push_two_last_value_is_head():
    """Test second push value is head's value."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.value == 'val2'


def test_linked_list_push_moves_old_head_to_new_heads_next():
    """Test push changes old head to new head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next_node.value == 'val'


def test_linked_list_pop_removes_head_and_returns_value():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    popped = l.pop()
    assert popped is 'potato'


def test_linked_list_returns_head_value():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    assert l.pop() == 'potato'


def test_linked_list_pop_shits_head_properly():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.value == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_length():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(10))
def test_linked_list_size_returns_length2(n):
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(10))
def test_linked_list_can_use_len_function(n):
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_with_one_node_returns_node():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search_with_one_node_bad_search():
    """Test search node not there with one node in list returns none."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).value == search_me


def test_linked_list_takes_iterable_and_has_values():
    """."""
    from linked_list import LinkedList
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).value == item


def test_remove_in_empty_list():
    """Test that removal from empty list raises error."""
    from linked_list import LinkedList
    with pytest.raises(ValueError):
        l = LinkedList()
        l.remove(1)


def test_linked_list_can_remove_value():
    """Test value can be removed."""
    from linked_list import LinkedList
    with pytest.raises(ValueError):
        l = LinkedList()
        for i in range(10):
            l.push(i)
        l.remove(l.search(6))


def test_remove_head_if_head_only_node():
    """Remove head node if only a head node, head should become none."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    l.remove(1)
    assert not l.head


def test_remove_not_head_node_no_longer_exists():
    """If removed node not head, check it not in list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    l.push(2)
    l.remove(1)
    assert not l.search(1)


def test_linked_list_display_method_displays_correctly():
    """Test display method displays correctly."""
    from linked_list import LinkedList
    l = LinkedList(['potato', 'cabbage', 'gruel'])
    assert l.display() == "(gruel, cabbage, potato)"
