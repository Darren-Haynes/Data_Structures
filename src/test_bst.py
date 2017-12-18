"""Tests for the Binary Search Tree."""

import pytest
from hash import HashTable

<<<<<<< HEAD

def test_default_hast_table_has_len_6(table6_add):
    """Default hash table should be Initialized with 6 buckets."""
    assert len(table6_add.table) == 6
=======
def test_tree_initiates_with_empty_root(empty_t):
    """Tree instantiated without iterables should be empty."""
    assert not empty_t.root
>>>>>>> c6508eb296c84c82aae470d888b55dafe388410f


def test_default_hash_table_buckets_are_empty(table6_add):
    """Default initiates to table with 6 empty buckets."""
    for bucket in table6_add.table:
        assert not bucket


<<<<<<< HEAD
def test_incorrect_hash_parameter_raises_error():
    """Test incorrect hash_type passed to constructor raises ValueError."""
    with pytest.raises(ValueError):
        HashTable(hash_type='not_a_hashing_type')
=======
# def test_tree_has_correct_size(empty_t):
    # """Emtpy tree should have size of 0."""
    # node_values = random.sample(range(1, 100), 50)
    # for i, val in enumerate(node_values, 1):
        # empty_t.insert(val)
        # assert empty_t.size() == i
>>>>>>> c6508eb296c84c82aae470d888b55dafe388410f


def test_set_key_method_raises_error(table6_add):
    """Key used in set_key method must be a string, else error."""
    with pytest.raises(TypeError):
        table6_add.set_key(1)


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
    table6_add.set_key(key, value)
    idx = table6_add._additive(key) % 6
    assert table6_add.table[idx][0][0] == key


@pytest.mark.parametrize('key, value', WORDS6)
def test_elf_words_filled_all_buckets(key, value, table6_elf):
    """Test that additive hash puts 6 words into each of the 6 buckets of a
    list that has just 6 buckets. There should be no collisions"""
    table6_elf.set_key(key, value)
    idx = table6_elf._elf(key) % 6
    assert table6_elf.table[idx][0][0] == key


def test_2_additive_words_in_same_bucket(table6_add):
    """2 different words with same hash should be in same bucket."""
    table6_add.set_key('apple', 'bob')
    table6_add.set_key('papel', 'fred')
    assert len(table6_add.table[2]) == 2
    assert ('apple', 'bob') in table6_add.table[2]
    assert ('papel', 'fred') in table6_add.table[2]


def test_2_additive_words_in_same_bucket_others_empty(table6_add):
    """2 different words with same hash; other buckets should be empty."""
    table6_add.set_key('apple', 'bob')
    table6_add.set_key('papel', 'fred')
    for idx in range(6):
        if idx != 2:
            assert not table6_add.table[idx]


def test_get_method_raises_error_if_bucket_exists(adt6_no_dups):
    """Trying to get non existant key from bucket that exist if key not
    there raises KeyError.
    """
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


<<<<<<< HEAD
def test_key_exists_if_bucket_length_greater_than_one(adt6_no_dups):
    """If bucket has more than one key/value pair it should return true
    if key exists."""
    adt6_no_dups.set_key('papel', 'hello there')
    assert adt6_no_dups.key_exists('papel', 2)


def test_key_not_string_raises_type_error(table6_add):
    """Test set method raises error if key not a string."""
    with pytest.raises(TypeError):
        table6_add.set_key(1, 2)


def test_key_already_exists_raises_key_error(table1key):
    """If key exists, KeyError should raise."""
    with pytest.raises(KeyError):
        table1key.set_key('apple', 'yummy')

def test_get_error_if_bucket_empty(table1key):
    """Test get key returns error if mapped bucket is empty."""
    with pytest.raises(KeyError):
        # import pdb; pdb.set_trace()
        table1key.get('a')

def test_get_for_bucket_with_just_one_key_pair(table1key):
    """If bucket contains just one key/balue pair get should work."""
    table1key.set_key('banana', 'hello')
    assert table1key.get('banana') == 'hello'

def test_get_in_collision_bucket(table1key):
    """If 2 key/pairs in bucket, get should retrieve correct pair."""
    table1key.set_key('papel', 'hello')
    assert table1key.get('papel') == 'hello'
=======

def test_tree_two_nodes_left_has_depth_one(one_t):
    """2 node tree with root child on left should have depth one."""
    one_t.insert(5)
    assert one_t.depth() == 1


def test_tree_two_nodes_right(one_t):
    """2 node tree with root child on right should have depth one."""
    one_t.insert(5)
    assert one_t.depth() == 1


def test_balanced_tree_with_3_nodes_has_depth_one(balanced_3_nodes):
    """Tree with 3 nodes balanced should have depth of 1."""
    assert balanced_3_nodes.depth() == 1


def test_tree_with_one_leaf_node_right_of_left_depth(balanced_3_nodes):
    """Balanced tree with 4 nodes and 4th leaf node is on left side of tree
    and right of parent has depth of 2."""
    balanced_3_nodes.insert(8)
    assert balanced_3_nodes.depth() == 2


def test_tree_with_one_leaf_node_left_of_right_depth(balanced_3_nodes):
    """Balanced tree with 4 nodes and 4th leaf node is on right side of tree
    and left of parent has depth of 2."""
    balanced_3_nodes.insert(13)
    assert balanced_3_nodes.depth() == 2


def test_balanced_tree_7_nodes_has_depth_two(balanced_7_nodes):
    """Balanced tree with 7 nodes depth should be 2."""
    assert balanced_7_nodes.depth() == 2


def test_empty_tree_contains(empty_t):
    """Empty tree contains should return appropriate string message."""
    empty_t.contains(1) == "An empty tree has no values."


def test_value_in_tree_returns_true(balanced_7_nodes):
    """If value in tree contains should return True."""
    assert balanced_7_nodes.contains(7)


def test_value_not_in_tree_returns_false(balanced_7_nodes):
    """If value not in tree contains should return false."""
    assert not balanced_7_nodes.contains(4)


def test_empty_tree_balance_returns_message(empty_t):
    """If tree is empty balance will return string message."""
    assert empty_t.balance() == "Empty tree has no balance."


def test_tree_with_one_node_balance_is_zero(one_t):
    """Tree with just one node should return balance of zero."""
    assert one_t.balance() == 0


def test_tree_2_nodes_left_unbalanced(one_t):
    """Tree with 2 nodes and left sided should return balance of 1."""
    one_t.insert(9)
    assert one_t.balance() == 1


def test_tree_2_nodes_right_unbalanced(one_t):
    """Tree with 2 nodes and right sided should return balance of 1."""
    one_t.insert(11)
    assert one_t.balance() == -1

def test_tree_3_nodes_balanced_return_1(balanced_3_nodes):
    """Tree with 3 balanced nodes should return balance of 0."""
    assert balanced_3_nodes.balance() == 0


def test_tree_4_nodes_left_unbalanced_return_1(balanced_3_nodes):
    """Tree with 3 balanced nodes should return balance of 0."""
    balanced_3_nodes.insert(8)
    assert balanced_3_nodes.balance() == 1


def test_tree_4_nodes_right_unbalanced_return_1(balanced_3_nodes):
    """Tree with 3 balanced nodes should return balance of 0."""
    balanced_3_nodes.insert(13)
    assert balanced_3_nodes.balance() == -1


def test_tree_7_nodes_balanced_return_1(balanced_7_nodes):
    """Tree with 7 balanced nodes should return balance of 0."""
    assert balanced_7_nodes.balance() == 0
>>>>>>> c6508eb296c84c82aae470d888b55dafe388410f
