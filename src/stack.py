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
        pop_node = self.stack.head
        if pop_node is None:
            raise IndexError("No nodes in stack")
        self.stack.head = pop_node.next_node
        pop_node.next_node = None
        self.stack._size -= 1
        return pop_node.value

    def __len__(self):
        """Get number of nodes in list."""
        return self.stack._size
