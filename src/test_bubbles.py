"""Tests for the Binary Search Tree."""

import random
import pytest
from bubble import bubble_sort


def random_100_lists():
    """Return 100 random lists."""
    lists = []
    for _ in range(100):
        rand_len = random.randint(2, 100)
        temp_lst = []
        for _ in range(rand_len):
            temp_lst.append(random.randint(0, 1000))
        lists.append((temp_lst, sorted(temp_lst)))
    return lists

RAND_BUBBLES = random_100_lists()


@pytest.mark.parametrize('input, output', RAND_BUBBLES)
def test_bubble_sort_sorts(input, output):
    """Bubbles."""
    assert bubble_sort(input) == output
