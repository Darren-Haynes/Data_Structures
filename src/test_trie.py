"""Test the Trie."""
import pytest
from faker import Faker
from trie import Trie

FAKE = Faker()


def test_trie_initiates_with_root_node(empty_trie):
    """Instantiate tree should have a root node."""
    assert empty_trie.root


def test_trie_root_node_value_is_star(empty_trie):
    """Instantiating trie should create node with a value '*'."""
    assert empty_trie.root.value == '*'


def test_trie_root_node_childen_is_empty_dict(empty_trie):
    """Instatiating trie should create root with children attribute as dict."""
    assert empty_trie.root.children == {}


def test_trie_root_node_end_is_false(empty_trie):
    """Instantiate trie, root 'end' attribute should be false."""
    assert not empty_trie.root.end


def test_trie_instatiates_with_size_zero(empty_trie):
    """Instantiate trie should have size of zero."""
    assert empty_trie._size == 0


def test_non_iter_passed_to_trie_raises_error():
    """Trie instantiated with string as iter raises Value."""
    with pytest.raises(TypeError):
        t = Trie('word')


def test_valid_iter_passed_increases_trie_size(trie_3):
    """Trie instantiated with valid iter should increase size."""
    assert trie_3._size == 3


def test_insert_not_string_raises_error(empty_trie):
    """A non string passed to insert should raise type error."""
    with pytest.raises(TypeError):
        empty_trie.insert(1)


def test_insert_string_trie_size_increases_correctly(empty_trie):
    """Trie size should increase by 1 for every word inserted."""
    for i in range(1, 51):
        empty_trie.insert(FAKE.word())
        assert empty_trie._size == i


def test_contains_raises_error(empty_trie):
    """Contain method should raise type error if passed non string."""
    with pytest.raises(TypeError):
        empty_trie.contains(1)
