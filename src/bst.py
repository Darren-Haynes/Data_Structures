"""Binary Search Tree."""

from queue import Queue
from stack import Stack


class Node(object):
    """Binary tree node."""

    def __init__(self, value=None):
        """Instantiate a node."""
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class Tree(object):
    """Binary Search Tree."""

    def __init__(self, iterable=None):
        """Initiate a binary search tree."""
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple, set)):
            for num in iterable:
                self.insert(num)

    def insert(self, value):
        """Insert value into the bst."""
        if not self.root:
            self.root = Node(value)
            self._size += 1
            return

        return self._insert(value, self.root)

    def _insert(self, value, node):
        """Recursive part of 'insert' function."""
        if value == node.value:
            raise ValueError("Value already exists")

        if value < node.value:
            if not node.left:
                node.left = Node(value)
                node.left.parent = node
                self._size += 1
                return
            return self._insert(value, node.left)

        if value > node.value:
            if not node.right:
                node.right = Node(value)
                node.right.parent = node
                self._size += 1
                return
            return self._insert(value, node.right)

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def depth(self):
        """Return depth of the tree."""
        if not self.root:
            return "Empty tree has no depth."
        return self._depth(self.root, -1)

    def _depth(self, curr_node, curr_depth):
        """Recurse until depth is found."""
        if not curr_node:
            return curr_depth
        left_depth = self._depth(curr_node.left, curr_depth + 1)
        right_depth = self._depth(curr_node.right, curr_depth + 1)
        return max(left_depth, right_depth)

    def contains(self, value):
        """Establish if a value exists in tree."""
        if not self.root:
            return "An empty tree has no values."
        else:
            return self._contains(self.root, value)

    def _contains(self, curr_node, value):
        """Recurse nodes to find value if it exists."""
        if curr_node.value == value:
            return True

        if value < curr_node.value and curr_node.left:
            return self._contains(curr_node.left, value)
        elif value > curr_node.value and curr_node.right:
            return self._contains(curr_node.right, value)

    def balance(self, node=None):
        """Return integer balance of the tree sides."""
        if not node:
            node = self.root
            if not node:
                return "Empty tree has no balance."""
            return self._depth(self.root.left, 0) \
                - self._depth(self.root.right, 0)
        return self._depth(node.left, 0) - self._depth(node.right, 0)

    def breadth(self):
        """Breadth search of tree."""
        if not self.root:
            print("Tree is empty")

        que = Queue()
        que.enqueue(self.root)
        # print(self.root.value)
        yield self.root.value

        while que:
            node = que.dequeue()
            if node.left:
                # print(node.left.value)
                yield node.left.value
                que.enqueue(node.left)

            if node.right:
                # print(node.right.value)
                yield node.right.value
                que.enqueue(node.right)

    def in_order(self):
        """Traverse the bst and yield node values in order."""
        if self.root is None:
            raise ValueError("Tree is empty")

        stack = Stack()
        curr = self.root
        while curr or stack:
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                yield curr.value
                curr = curr.right

    def _right_rotation(self, node):
        """Operate a right rotation to balance bst."""
        if node.parent == self.root:
            self.root.left = node.right
            if self.root.left:
                self.root.left.parent = self.root
            node.right = node.parent
            node.right.parent = node
            node.parent = None
            self.root = node
        else:
            node.parent.left = node.right
            if node.parent.parent.left == node.parent:
                node.parent.parent.left = node
            else:
                node.parent.parent.right = node
            if node.right:
                node.right.parent = node.parent
            node.right = node.parent
            node.parent = node.parent.parent

    def _left_rotation(self, node):
        """Opperate a left rotation to balance bst."""
        if node.parent == self.root:
            self.root.right = node.left
            if self.root.right:
                self.root.right.parent = self.root
            node.left = node.parent
            node.left.parent = node
            node.parent = None
            self.root = node
        else:
            node.parent.right = node.left
            if node.parent.parent.right == node.parent:
                node.parent.parent.right = node
            else:
                node.parent.parent.left = node
            if node.left:
                node.left.parent = node.parent
            node.left = node.parent
            node.parent = node.parent.parent

    def _balance(self, node):
        """Balance bst."""
        while node:
            if self.balance(node) > 1:
                if self.balance(node.left) >= 0:
                    self._right_rotation(node.left)
                else:
                    node = node.left.right
                    self._left_rotation(node)
                    self._right_rotation(node)
            elif self.balance(node) < -1:
                if self.balance(node.right) <= 0:
                    self._left_rotation(node.right)
                else:
                    node = node.right.left
                    self._right_rotation(node)
                    self._left_rotation(node)
            else:
                node = node.parent

    def create_balanced_7_node(self):  # pragma: no cover
        """Create blanced tree with 7 nodes."""
        self.insert(10)
        self.insert(5)
        self.insert(15)
        self.insert(20)
        self.insert(13)
        self.insert(3)
        self.insert(7)

    def create_unbalanced_9_node(self):  # pragma: no cover
        """Create unblanced tree with 7 nodes."""
        self.insert(5)
        self.insert(2)
        self.insert(6)
        self.insert(4)
        self.insert(7)
        self.insert(1)
        self.insert(9)
        self.insert(3)
        self.insert(8)
