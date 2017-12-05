"""Test fixtures for the hash table tests."""

import pytest
from hash import HashTable


@pytest.fixture()
def table6_add():
    """Initialize table with 6 buckets."""
    t = HashTable()
    return t


@pytest.fixture()
def table6_elf():
    """Initialize table with 6 buckets."""
    t = HashTable(hash_type='elf')
    return t

@pytest.fixture()
def table1key():
    """Table with just 1 key/pair."""
    t = HashTable()
    t.set_key('apple', 'chapel')
    return t


@pytest.fixture()
def words_list():
    """Big ass list of dictionary words."""
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    return words


@pytest.fixture()
def adt6_no_dups():
    t = HashTable()
    t.set_key('aaaaaa', 'bettie')
    t.set_key('a', 'bettie')
    t.set_key('apple', 'bob')
    t.set_key('potato', 'fred')
    t.set_key('spinach', 'james')
    t.set_key('sweet potato', 'jenny')
    return t

