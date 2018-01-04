"""Tests for the stack."""

import pytest


def test_stack_had_head():
    """A new stack should have a head."""
    from stack import Stack
    l = Stack()
    assert l.stack.head is None


def test_stack_push_adds_new_item():
    """Linded List push method should add a new item to the list."""
    from stack import Stack
    l = Stack()
    l.push('val')
    assert l.stack.head.value == 'val'


def test_stack_push_two_last_value_is_head():
    """Test second push value is head's value."""
    from stack import Stack
    l = Stack()
    l.push('val')
    l.push('val2')
    assert l.stack.head.value == 'val2'


def test_stack_push_moves_old_head_to_new_heads_next():
    """Test push changes old head to new head."""
    from stack import Stack
    l = Stack()
    l.push('val')
    l.push('val2')
    assert l.stack.head.next_node.value == 'val'


def test_stack_pop_removes_head_and_returns_value():
    """Test stack pops head and returns value."""
    from stack import Stack
    l = Stack()
    l.push('potato')
    popped = l.pop()
    assert popped is 'potato'


def test_stack_returns_head_value():
    """Test stack returns head's value."""
    from stack import Stack
    l = Stack()
    l.push('potato')
    assert l.pop() == 'potato'


def test_stack_pop_shits_head_properly():
    """Test pop shifts correct value back to head."""
    from stack import Stack
    l = Stack()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.stack.head.value == 'potato'


def test_stack_pop_empty_raises_exception():
    """Empty stack shouls raise index error on pop."""
    from stack import Stack
    l = Stack()
    with pytest.raises(IndexError):
        l.pop()


@pytest.mark.parametrize('n', range(10))
def test_stack_can_use_len_function(n):
    """Test multiple size uses __len__ method."""
    from stack import Stack
    l = Stack()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_stack_takes_iterable_and_has_values():
    """Test stack takes an iterable and implements it correctly."""
    from stack import Stack
    a_list = [5, 2, 9, 0, 1]
    l = Stack(a_list)
    for item in reversed(a_list):
        p = l.pop()
        assert p == item
