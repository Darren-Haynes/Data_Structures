"""Test the binary heap."""


import pytest


def test_heap_list_initiated_with_length_one(eh):
    """Heap list should be instatiated with single value of None."""
    assert len(eh.heap) == 1


def test_heap_initiates_with_list_with_single_index_containing_none(eh):
    """When instantiating a new heap it should have one item: None."""
    assert not eh.heap[0]


def test_push_value_increases_len_of_list_by_one_each_time(eh):
    """Pushing values creates correct list lengths."""
    for i in range(10):
        eh.push(i)
        assert len(eh.heap) == i + 2


def test_type_error_raised_when_non_numbers_passed_into_iterable(eh):
    """If iterable contains non numbers, raise TypeError."""
    from binary_heap import BinaryHeap
    with pytest.raises(TypeError):
        BinaryHeap([1, 2, 'non number'])


def test_iterable_becomes_attribute_if_passed_as_argument(eh):
    """An iterable in our case is limited to list, tuple."""
    from binary_heap import BinaryHeap
    b = BinaryHeap([1, 2, 3])
    c = BinaryHeap((1, 2, 3))
    assert type(b.iterable) == list
    assert type(c.iterable) == tuple


TABLE4 = [
    ([20, 15, 10, 5], [None, 20, 15, 10, 5]),
    ((5, 10, 15, 20), [None, 20, 15, 10, 5]),
    ([20, 5, 10, 15], [None, 20, 15, 10, 5]),
    ((5, 15, 10, 20), [None, 20, 15, 10, 5])
]


@pytest.mark.parametrize('iterable, result', TABLE4)
def test_same_input_in_different_order_heaps_correctlt(iterable, result):
    """Pass in same 4 numbers in different order and see if push works."""
    from binary_heap import BinaryHeap
    b = BinaryHeap(iterable)
    assert b.heap == result


def test_pop_empty_heap_raises_index_error(eh):
    """Emtpy heap should raise Index Error."""
    assert not eh.pop()


# @pytest.mark.parametrize('iterable, result', TABLE4)
def test_pop_returns_value_at_top_of_heap(eh):
    """Pop should return the value at the top of the heap."""
    eh.push(1000)
    assert eh.pop() == 1000


TYPES = [1, '1', {1: 'one'}]


def test_correct_input_passed_on_heap_instantiation():
    """If anything other than tuple or list passed, raise TypeError."""
    from binary_heap import BinaryHeap
    for t in TYPES:
        with pytest.raises(TypeError):
            BinaryHeap(t)


def test_pop_returns_sorted_values():
    """Test pop entire bin returns sorted values."""
    from binary_heap import BinaryHeap
    import random
    rand_nums = list(set([random.randint(0, 1000000000)
                     for i in range(10000)]))
    b = BinaryHeap(rand_nums)
    # import pdb; pdb.set_trace()
    all_popped = [b.pop() for i in range(1, len(b.heap))]
    assert all_popped == sorted(rand_nums, reverse=True)


def test_push_raises_type_error():
    """If anything besides int, float or string given to push, raise error."""
    from binary_heap import BinaryHeap
    b = BinaryHeap()
    with pytest.raises(TypeError):
        b.push([1, 2, 3])
