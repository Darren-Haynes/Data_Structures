"""Double-ended queue module."""


class Node(object):
    """Simple node for use by the deque."""

    def __init__(self, value):
        """Create a node for the deque."""
        self.value = value
        self.next_node = None
        self.prev_node = None


class Deque(object):
    """Deque class implementation."""

    def __init__(self):
        """Initiate empty deque."""
        self.end = None
        self.front = None
        self._size = 0

    def append(self, val):
        """Add value to the end of the deque."""
        if self._size == 0:
            return self.appendonly(val)
        new_node = Node(val)
        self.end.prev_node = new_node
        new_node.next_node = self.end
        self.end = new_node
        self._size += 1

    def appendleft(self, val):
        """Add a value to the front of the deque."""
        if self._size == 0:
            return self.appendonly(val)
        new_node = Node(val)
        self.front.next_node = new_node
        new_node.prev_node = self.front
        self.front = new_node
        self._size += 1

    def appendonly(self, val):
        """Used by append and appendleft to add node to an empty deque."""
        self.end = self.front = Node(val)
        self._size = 1

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        if self._size == 0:
            raise IndexError
        if self._size == 1:
            return self.poponly()
        the_node = self.end
        self.end = self.end.next_node
        self.end.prev_node = None
        self._size -= 1
        return the_node.value

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        if self._size == 0:
            raise IndexError
        if self._size == 1:
            return self.poponly()
        the_node = self.front
        self.front = self.front.prev_node
        self.front.next_node = None
        self._size -= 1
        return the_node.value

    def poponly(self):
        """Used by pop and popleft to remove the only node in the deque."""
        the_node = self.end
        self.end = self.front = None
        self._size = 0
        return the_node.value

    def peek(self):
        """Return the next value that would be returned by pop."""
        if self.end:
            return self.end.value
        return None

    def peekleft(self):
        """Return the next value that would be returned by popleft."""
        if self.front:
            return self.front.value
        return None

    def size(self):
        """Return the count of items in the queue."""
        return self._size
