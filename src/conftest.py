"""Test fixtures for the binary search tree tests."""

import pytest
from hash import HashTable


@pytest.fixture()
def table6():
    """Initialize table with 6 buckets."""
    t = HashTable()
    return t


@pytest.fixture()
def words_list():
    """Big ass list of dictionary words."""
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    return words

# @pytest.fixture()
# def adt6_no_dups():
    # t.set_table('aaaaaaa', 'bettie')
    # t.set_table('a', 'bettie')
    # t.set_table('apple', 'bob')
    # t.set_table('potato', 'fred')
    # t.set_table('spinach', 'james')
    # t.set_table('sweet potato', 'jenny')
# ]

