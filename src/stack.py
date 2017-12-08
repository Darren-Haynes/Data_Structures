"""Stack Data Structure."""

from linked_list import LinkedList


class Stack(object):
    """The Stack Object."""

    def __init__(self, itr=()):
        """Instantiate an empty stack."""
        self.stack = LinkedList(itr)

    def push(self, val):
        """Push a value into the stack."""
        self.stack.push(val)

    def pop(self):
        """Pop last value pushed into stack, if stack not empty."""
        return self.stack.pop()

    def __len__(self):
        """Get number of nodes in list."""
        return self.stack._size
