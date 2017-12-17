"""A double-ended linked list."""


class Node(object):
    """The node object. All methods are in the DoublyLinkedList class."""

    def __init__(self, val=None):
        """Create a node for the list."""
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    """Linked list traversable in both directions."""

    def __init__(self):
        """Initiate an empty list."""
        self.tail = None
        self.head = None
        self._size = 0

    def __len__(self):
        """Return size of the list."""
        return self._size

    def push(self, val):
        """Add a new node to the head of the list."""
        new_node = Node(val)
        if self._size == 0:
            self.list_begins(new_node)
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self._size += 1

    def append(self, val):
        """Add a new node to the tail."""
        new_node = Node(val)
        if self._size == 0:
            self.list_begins(new_node)
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def list_begins(self, node):
        """Function called by push and append to add to an empty list."""
        self.tail = node
        self.head = node
        self._size += 1

    def pop_single_node(self):
        """Pop when there is only one node in the list."""
        single_node = self.head
        self.head = None
        self.tail = None
        self._size -= 1
        return single_node.val

    def pop(self):
        """Take and return the node at the head of the list."""
        if self._size == 0:
            raise IndexError("Empty list, nothing to pop")
        elif self._size == 1:
            return self.pop_single_node()
        the_head = self.head
        self.head = self.head.next
        self.head.prev = None
        self._size -= 1
        return the_head.val

    def shift(self):
        """Take and return the node at the tail."""
        if self._size == 0:
            raise IndexError("Empty list, nothing to pop")
        elif self._size == 1:
            return self.pop_single_node()
        the_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1
        return the_tail.val

    def remove(self, value):
        """Remove the first node with the given value."""
        current = self.head
        while current:
            if current.val == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return
            current = current.next
        raise ValueError('Value not in list')
