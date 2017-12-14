"""Pytest fixures."""
import pytest
from double_linked_list import DoublyLinkedList

@pytest.fixture
def dll_no_nodes():
    return DoublyLinkedList()


@pytest.fixture
def dll_three_nodes():
    dll = DoublyLinkedList()
    dll.push('sugar glider')
    dll.push('dog')
    dll.push('cat')
    return dll
