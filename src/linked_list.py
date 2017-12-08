"""Linked list module."""


class Node(object):
    """Individual list nodes. All methods are in the Linked_List class."""

    def __init__(self, val=None):
        """Instantiate a node."""
        self.next_node = None
        self.value = val


class LinkedList(object):
    """A singly-linked list."""

    def __init__(self, itr=()):
        """Instantiate list with option for iterable."""
        self.head = None
        self._size = 0
        if isinstance(itr, (str, tuple, list)):
            for item in itr:
                self.push(item)

    def push(self, val):
        """Add a new node to the head of the list."""
        new_head = Node(val)
        new_head.next_node = self.head
        self.head = new_head
        self._size += 1

    def pop(self):
        """Take and return the node at the head of the list."""
        pop_node = self.head
        if pop_node is None:
            raise IndexError("No nodes in list")
        self.head = pop_node.next_node
        pop_node.next_node = None
        self._size -= 1
        return pop_node.value

    def size(self):
        """Get the number of nodes in the list."""
        return self._size

    def __len__(self):
        """Get the number of nodes in the list. Used by len()."""
        return self.size()

    def search(self, val):
        """Find the first node in the list with the given value."""
        search_node = self.head
        while(search_node):
            if search_node.value == val:
                return search_node
            search_node = search_node.next_node
        return None

    def remove(self, value):
        """Remove the given node from the list."""
        if not self.head:
            raise ValueError("List is empty, there is nothing to remove")

        if self.head.value == value:
            self.head = self.head.next_node
            return

        curr_node = self.head.next_node
        prev_node = self.head
        while curr_node:
            if curr_node.value == value:
                prev_node.next_node = curr_node.next_node
                return
            prev_node = curr_node
            curr_node = curr_node.next_node

        raise ValueError("Value not in list")

    def display(self):
        """Display the contents of the list in the format of a tuple."""
        string_list = "("
        current_node = self.head
        while current_node:
            string_list = string_list + str(current_node.value)
            if current_node.next_node:
                string_list = string_list + ", "
            current_node = current_node.next_node

        string_list = string_list + ")"
        return string_list

    def create_list_with_10_nodes(self):  # pragma: no cover
        """Create a node with values 1 to 10."""
        for i in range(1, 11):
            self.push(i)
