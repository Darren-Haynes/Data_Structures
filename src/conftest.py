"""Test fixtures for the binary search tree tests."""

import pytest
from bst import Tree


@pytest.fixture()
def empty_t():
    """Create empty tree."""
    return Tree()


@pytest.fixture()
def one_t():
    """Create tree with one node."""
    t = Tree()
    t.insert(10)
    return t


@pytest.fixture()
def balanced_3_nodes():
    """Create balanced tree with 3 nodes."""
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    return t


@pytest.fixture()
def balanced_7_nodes():
    """Create balanced tree with 3 nodes."""
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(20)
    t.insert(13)
    t.insert(3)
    t.insert(7)
    return t
