"""Test Deque."""
import pytest


def test_append_left_appends_front(deque_no_nodes):
    """Test that append left pushes value to the front."""
    deque_no_nodes.appendleft('a')
    assert deque_no_nodes.front.value == 'a'


def test_append_appends_to_end(deque_no_nodes):
    """Test that append left pushes value to the front."""
    deque_no_nodes.append('a')
    assert deque_no_nodes.end.value == 'a'


def test_pop_raises_index_error_when_deque(deque_no_nodes):
    """Test pop raise index error when popping empty deque."""
    with pytest.raises(IndexError):
        deque_no_nodes.pop()


def test_popleft_raises_index_error_when_deque(deque_no_nodes):
    """Test popleft raise index error when popping empty deque."""
    # from server import parse_request
    with pytest.raises(IndexError):
        deque_no_nodes.popleft()


def test_pop_removes_from_end_of_list_when_only_one_node(deque_no_nodes):
    """Test that pop removes value from end of deque."""
    deque_no_nodes.append('a')
    assert deque_no_nodes.end.value == deque_no_nodes.pop()


def test_pop_removes_from_front_of_list_when_node_appended(deque_no_nodes):
    """Test that pop removes value from front of deque."""
    deque_no_nodes.append('a')
    assert deque_no_nodes.front.value == deque_no_nodes.pop()


def test_pop_removes_from_end_when_one_node_has_been_appended(deque_no_nodes):
    """Test pop removes correct value from end of deque, when only 1 node."""
    deque_no_nodes.append('a')
    assert deque_no_nodes.end.value == deque_no_nodes.pop()


def test_pop_removes_from_start_when_one_node_appendedleft(deque_no_nodes):
    """Test that pop removes value from front of deque."""
    deque_no_nodes.appendleft('a')
    assert deque_no_nodes.front.value == deque_no_nodes.pop()


def test_pop_removes_from_end_when_one_node_appendedleft(deque_no_nodes):
    """Test that pop removes value from end of deque."""
    deque_no_nodes.appendleft('a')
    assert deque_no_nodes.end.value == deque_no_nodes.pop()


def test_pop_removes_from_end_of_list_when_theres_2_nodes(deque_no_nodes):
    """Test that pop removes value from end of deque when 2 nodes."""
    deque_no_nodes.append('a')
    deque_no_nodes.append('b')
    assert deque_no_nodes.end.value == deque_no_nodes.pop()


def test_popleft_removes_from_end_of_list_when_only_one_node_has_has_been_appendedleft(deque_no_nodes):
    """Test that pop removes value from end of deque."""
    deque_no_nodes.appendleft('a')
    assert deque_no_nodes.end.value == deque_no_nodes.popleft()


def test_popleft_removes_from_start_of_list_when_theres_2_nodes(
        deque_no_nodes):
    """Test that popleft removes value from end of deque when 2 nodes."""
    deque_no_nodes.appendleft('a')
    deque_no_nodes.appendleft('b')
    assert deque_no_nodes.front.value == deque_no_nodes.popleft()


def test_peek_sees_the_same_value_that_pop_does(deque_append_two):
    """Test with 2 nodes in deque, as 1 node can been seen from either side."""
    assert 'a' == deque_append_two.pop()


def test_peekleft_sees_the_same_value_that_popleft_does(deque_append_two):
    """Test with 2 nodes in deque, as 1 node can been seen from either side."""
    assert deque_append_two.front.value == deque_append_two.popleft()


def test_peek_sees_end_if_end_exists(deque_no_nodes):
    """Test that peed sees the value at end of deque."""
    deque_no_nodes.append('a')
    assert 'a' == deque_no_nodes.peek()


def test_peek_sees_front_if_deque_empty(deque_no_nodes):
    """Test that peed sees None if deque empty."""
    assert not deque_no_nodes.peek()


def test_peek_sees_none_if_deque_empty(deque_no_nodes):
    """Test that peek sees None if deque empty."""
    assert not deque_no_nodes.peek()


def test_peekleft_sees_front_if_front_exists(deque_no_nodes):
    """Test that peed sees the value at front of deque."""
    deque_no_nodes.appendleft('a')
    assert 'a' == deque_no_nodes.peekleft()


def test_peekleft_sees_none_if_deque_empty(deque_no_nodes):
    """Test that peed sees None if deque empty."""
    assert not deque_no_nodes.peekleft()


def test_size_none_in_empty_deque(deque_no_nodes):
    """If deque empty size should be 0."""
    assert deque_no_nodes.size() == 0


def test_size_for_multiple_input(deque_no_nodes):
    """Test if multiple appends, size increases accordingly."""
    for i in range(10):
        deque_no_nodes.appendleft(i)
        assert deque_no_nodes.size() == i + 1
