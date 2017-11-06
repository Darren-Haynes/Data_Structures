"""Test the Priority Queue."""


import pytest
from random import randint


def test_q_instantiates_a_dict(empty_q):
    """Creation of PriorityQ object should instantiate a dictionary."""
    assert type(empty_q.queue) == dict


def test_q_insantiates_dict_of_length_1(empty_q):
    """Instantaited dict should contain one key:value pair. so length = 1."""
    assert len(empty_q.queue) == 1


def test_q_instantiates_with_0_as_first_priority(empty_q):
    """Q should have '0' as its first priority."""
    assert 0 in empty_q.queue


def test_q_instantiates_with_empty_list(empty_q):
    """Test Q instantiates with 0 as key and empty list as value."""
    assert empty_q.queue[0] == []


def test_q_instantiates_with_highest_as_0(empty_q):
    """Q should instantiate with '_highest' values of zeros."""
    assert empty_q._highest2 == [0, 0]


def test_q_instantiates_with_lowest_as_zeroes(empty_q):
    """Q should instantiate with '_lowest' values of zeros."""
    assert empty_q._lowest2 == [0, 0]


NOT_INTS = [
    ('a', 1.2),
    ('a', 'a'),
    ('a', (0, 2)),
    ('a', []),
    ('a', {}),
    ('a', False),
]


@pytest.mark.parametrize('val, priority', NOT_INTS)
def test_insert_is_passed_valid_priority(val, priority, empty_q):
    """Raise TypeError if priority passed as param is not integer."""
    with pytest.raises(TypeError):
        empty_q(val, priority)


def test_priority_param_is_int_returns_true(empty_q):
    """If int passed as priority param function returns true."""
    assert empty_q.insert('a', 1) == True


def test_priority_as_int_not_raise_error(empty_q):
    """Don't raise TypeError if integer passed as param for priority."""
    assert empty_q.insert('a', 1) != TypeError


def test_first_vals_inserted_with_default_priority_appends_correctly(empty_q):
    """When priority instantiated, first vals inserted using default priority 0
    should append to list that starts out empty."""
    for i in range(10):
        empty_q.insert(i)
    assert empty_q.queue[0][i] == i


def test_priority_not_in_dict_create_priority(empty_q):
    """If priority not in dict, create it with dict value being a 1 index list
    containing val param passed in."""
    empty_q.insert('a', 1)
    assert 1 in empty_q.queue
    assert empty_q.queue[1][0] == 'a'


def test_exisiting_priority_with_numerous_vals_appended(empty_q):
    """Test that multiple appends to same existing priority works."""
    for i in range(10):
        empty_q.insert(i)
        assert empty_q.queue[0][-1] == i


def test_new_priority_with_numerous_vals_appended(empty_q):
    """Test that multiple appends to newly created priority works."""
    empty_q.insert(10, 1)
    for i in range(10):
        empty_q.insert(i, 1)
        assert empty_q.queue[1][-1] == i


def test_multiple_new_prioritys_get_created_correctly(empty_q):
    """Check 10 new priorities are created with single value."""
    for i in range(1, 11):
        empty_q.insert('a', i)
        assert i in empty_q.queue
        assert empty_q.queue[i][-1] == 'a'


def test_multiple_values_append_to_10_priorities(q10):
    """Check that multiple values append to 10 unique priorities."""
    for priority in q10.queue:
        for i in range(10):
            q10.queue[priority].append(i)
            assert q10.queue[priority][-1] == i


def test_highest_priority_is_highest_priority(empty_q):
    """Check that 'self_lowest' is the lowest priority in dict."""
    for i in range(20):
        empty_q.insert(i, randint(-1000, 1000))
    assert empty_q._highest2[1] == max(empty_q.queue, key=int)


def test_lowest_priority_is_lowest_priority(empty_q):
    """Check that 'self_lowest' is the lowest priority in dict."""
    for i in range(20):
        empty_q.insert(i, randint(-1000, 1000))
    assert empty_q._lowest2[1] == min(empty_q.queue, key=int)


# def t
