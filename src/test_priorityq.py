"""Test the Priority Queue."""


import pytest


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
    """Q should instatiate with '_highest' value of 0."""
    assert empty_q._highest == 0


def test_q_instantiates_with_lowest_as_0(empty_q):
    """Q should instantiate with '_lowest' value of 0."""
    assert empty_q._lowest == 0


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

