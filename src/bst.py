"""Binary Search Tree."""


class Node(object):
    """Binary tree node."""

    def __init__(self, value=None):
        """Instantiate a node."""
        self.left = None
        self.right = None
        self.value = value


class Tree(object):
    """Binary Search Tree."""

    def __init__(self):
        """Initiate empty tree."""
        self.root = None
        self._size = 0

    def insert(self, data):
        """Insert a node into the tree."""
        if self.root:
            self._insert(data, self.root)
        else:
            self.root = Node(data)
            self._size += 1

    def _insert(self, data, curr_node):
        """."""
        if data < curr_node.value:
            if curr_node.left:
                self._insert(data, curr_node.left)
            else:
                curr_node.left = Node(data)
                self._size += 1

        if data > curr_node.value:
            if curr_node.right:
                self._insert(data, curr_node.right)
            else:
                curr_node.right = Node(data)
                self._size += 1

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def depth(self):
        """Return depth of the tree."""
        if not self.root:
            return "Empty tree has no depth."
        else:
            return self._depth(self.root, -1)

    def _depth(self, curr_node, curr_depth):
        """Recurse until depth is found."""
        if curr_node == None:
            return curr_depth
        left_depth = self._depth(curr_node.left, curr_depth + 1)
        right_depth = self._depth(curr_node.right, curr_depth + 1)
        return max(left_depth, right_depth)

    def search(self, value):
        """Establish if a value exists in tree."""
        if not self.root:
            return "An empty tree has no values."
        else:
            found = self._search(self.root, value)

        if found:
            return True
        else:
            return False

    def _search(self, curr_node, value):
        """Recurse nodes to find value if it exists."""
        if curr_node.value == value:
            return True

        if value < curr_node.value and curr_node.left:
            return self._search(curr_node.left, value)
        elif value > curr_node.value and curr_node.right:
            return self._search(curr_node.right, value)

    def balance(self):
        """Return integer balance of the tree sides."""
        if not self.root:
            return "Empty tree has no balance."""

        if self.size() == 1:
            return 0
        else:
            return self._balance(self.root, 0)

    def _balance(self, curr_node, count):
        """Recurse to calculate balance."""
        if not curr_node:
            return count

        return self._balance(curr_node.left, count + 1)
        return self._balance(curr_node.right, count - 1)


