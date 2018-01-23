"""Tests for the Binary Search Tree."""

import pytest
import random
from bst import Tree

def test_tree_initiates_with_empty_root(empty_t):
    """Tree instantiated without iterables should be empty."""
    assert not empty_t.root


def test_empty_tree_size_is_zero(empty_t):
    """Emtpy tree size should be zero."""
    assert empty_t.size() == 0


def test_tuple_passed_as_iterable():
    """Tuple passed as interable should populate the tree"""
    tree = Tree((10, 5, 100))
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 100


def test_list_passed_as_iterable():
    """List passed as interable should populate the tree"""
    tree = Tree([10, 5, 100])
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 100


def test_set_passed_as_iterable():
    """Set passed as interable should populate the tree"""
    tree = Tree([10, 5, 100])
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 100


def test_tree_with_one_node_root_exists(one_t):
    """Root of tree should exist if it has one node."""
    assert one_t.root


def test_tree_with_one_node_root_no_children(one_t):
    """Tree with one node, root should have no kids."""
    assert not one_t.root.left
    assert not one_t.root.right


def test_tree_with_one_node_has_correct_value(one_t):
    """If one node in tree, root node should have inserted value."""
    assert one_t.root.value == 10


def test_left_sided_tree_with_two_nodes_root_has_child(empty_t):
    """If 2 nodes in left sided tree, root points to left child only."""
    empty_t.insert(10)
    empty_t.insert(5)
    assert empty_t.root.left
    assert not empty_t.root.right


def test_right_sided_tree_with_two_nodes_root_has_child(empty_t):
    """If 2 nodes in right sided tree, root points to right child only."""
    empty_t.insert(10)
    empty_t.insert(15)
    assert empty_t.root.right
    assert not empty_t.root.left


def test_balanced_tree_with_3_nodes_root_has_2_kids(balanced_3_nodes):
    """Test balanced tree with 3 nodes, root has left and right kids."""
    assert balanced_3_nodes.root.right
    assert balanced_3_nodes.root.left


def test_balanced_tree_with_3_nodes_childens_values(balanced_3_nodes):
    """Balanced tree with 3 nodes, check root children's values are correct."""
    assert balanced_3_nodes.root.right.value == 15
    assert balanced_3_nodes.root.left.value == 5


def test_balanced_tree_with_7_nodes_is_correct(balanced_7_nodes):
    """Balanced tree with 5 nodes, nodes in right place."""
    root = balanced_7_nodes.root
    assert root.value == 10
    assert root.left.value == 5
    assert root.right.value == 15
    assert root.left.left.value == 3
    assert root.left.right.value == 7
    assert root.right.right.value == 20
    assert root.right.left.value == 13


def test_empty_tree_depth(empty_t):
    """Empty tree should return correct string message."""
    assert empty_t.depth() == "Empty tree has no depth."


def test_tree_one_node_has_depth_zero(one_t):
    """Tree with one node should have depth of zero."""
    assert one_t.depth() == 0


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


def test_insert_if_node_value_exist(balanced_3_nodes):
    """If node in tree insert should raise value error."""
    with pytest.raises(ValueError):
        balanced_3_nodes.insert(10)


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
