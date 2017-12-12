"""Tests for the Binary Search Tree."""

import pytest
from hash import HashTable


def test_default_hast_table_has_len_6(table6_add):
    """Default hash table should be Initialized with 6 buckets."""
    assert len(table6_add.table) == 6


def test_default_hash_table_buckets_are_empty(table6_add):
    """Default initiates to table with 6 empty buckets."""
    for bucket in table6_add.table:
        assert not bucket


def test_incorrect_hash_parameter_raises_error():
    """Test incorrect hash_type passed to constructor raises ValueError."""
    with pytest.raises(ValueError):
        HashTable(hash_type='not_a_hashing_type')


def test_set_table_method_raises_error(table6_add):
    """Key used in set_table method must be a string, else error."""
    with pytest.raises(TypeError):
        table6_add.set_table(1)


WORDS6 = [
    ('aaaaaaa', 'bettie'),
    ('a', 'bettie'),
    ('apple', 'bob'),
    ('potato', 'fred'),
    ('spinach', 'james'),
    ('sweet potato', 'jenny'),
]


@pytest.mark.parametrize('key, value', WORDS6)
def test_addtive_words_filled_all_buckets(key, value, table6_add):
    """Test that additive hash puts 6 words into each of the 6 buckets of a
    list that has just 6 buckets. There should be no collisions.
    """
    table6_add.set_table(key, value)
    idx = table6_add._additive(key) % 6
    assert table6_add.table[idx][0][0] == key


@pytest.mark.parametrize('key, value', WORDS6)
def test_elf_words_filled_all_buckets(key, value, table6_elf):
    """Test that additive hash puts 6 words into each of the 6 buckets of a
    list that has just 6 buckets. There should be no collisions"""
    table6_elf.set_table(key, value)
    idx = table6_elf._elf(key) % 6
    assert table6_elf.table[idx][0][0] == key


def test_2_additive_words_in_same_bucket(table6_add):
    """2 different words with same hash should be in same bucket."""
    table6_add.set_table('apple', 'bob')
    table6_add.set_table('papel', 'fred')
    assert len(table6_add.table[2]) == 2
    assert ('apple', 'bob') in table6_add.table[2]
    assert ('papel', 'fred') in table6_add.table[2]


def test_2_additive_words_in_same_bucket_others_empty(table6_add):
    """2 different words with same hash; other buckets should be empty."""
    table6_add.set_table('apple', 'bob')
    table6_add.set_table('papel', 'fred')
    for idx in range(6):
        if idx != 2:
            assert not table6_add.table[idx]


def test_get_method_raises_error_if_bucket_exists(adt6_no_dups):
    """Trying to get non existant key from bucket that exist if key not
    there raises KeyError."""
    with pytest.raises(KeyError):
        adt6_no_dups.get('banana')


def test_get_method_raises_error_if_bucket_empty(adt6_no_dups):
    """Raise key Error if hash index doesn't exist."""
    with pytest.raises(KeyError):
        adt6_no_dups.get('banana')

WORDS6IDX = [
    ('aaaaaa', 0),
    ('a', 1),
    ('apple', 2),
    ('potato', 3),
    ('spinach', 4),
    ('sweet potato', 5)
]


@pytest.mark.parametrize('key, idx', WORDS6IDX)
def test_key_exists_if_bucket_length_is_one(key, idx, adt6_no_dups):
    """Test key exists in bucket that contains only one key/value pair."""
    assert adt6_no_dups.key_exists(key, idx)


def test_key_exists_if_bucket_length_greater_than_one(adt6_no_dups):
    """If bucket has more than one key/value pair it should return true
    if key exists."""
    adt6_no_dups.set_table('papel', 'hello there')
    assert adt6_no_dups.key_exists('papel', 2)


def test_key_not_string_raises_type_error(table6_add):
    """Test set method raises error if key not a string."""
    with pytest.raises(TypeError):
        table6_add.set_table(1, 2)


# def test_key_already_exists_raises_key_error()