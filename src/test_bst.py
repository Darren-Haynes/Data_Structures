"""Tests for the Binary Search Tree."""

import pytest
import random


def test_default_hast_table_has_len_6(table6):
    """Default hash table should be Initialized with 6 buckets."""
    assert len(table6.table) == 6


def test_default_hash_table_bucket_are_empty(table6):
    """Default initiates to table with 6 empty buckets."""
    for bucket in table6.table:
        assert not bucket


ADDIITIVES = [
    ('aaaaaaa', 'bettie'),
    ('a', 'bettie'),
    ('apple', 'bob'),
    ('potato', 'fred'),
    ('spinach', 'james'),
    ('sweet potato', 'jenny'),
]


@pytest.mark.parametrize('key, value', ADDIITIVES)
def test_addtive_words_filled_all_buckets(key, value, table6):
    """Test that additive hash puts 6 words into each of the 6 buckets of a
    list that has just 6 buckets. There should be no collisions"""
    table6.set_table(key, value)
    idx = table6._additive(key) % 6
    # import pdb;pdb.set_trace()
    assert table6.table[idx][0][0] == key


def test_2_additive_words_in_same_bucket(table6):
    """2 different words with same hash should be in same bucket."""
    table6.set_table('apple', 'bob')
    table6.set_table('papel', 'fred')
    assert len(table6.table[2]) == 2
    assert ('apple', 'bob') in table6.table[2]
    assert ('papel', 'fred') in table6.table[2]
