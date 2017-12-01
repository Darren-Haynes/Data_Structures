"""Test fixtures for the binary search tree tests."""

import pytest
from hash import HashTable


@pytest.fixture()
def table6():
    """Initialize table with 6 buckets."""
    t = HashTable()
    return t

