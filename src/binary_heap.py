"""A Max Binary Heap."""

from __future__ import division


class BinaryHeap(object):
    """Binary Heap Class."""

    def __init__(self, iterable=None):
        """Instantiate heap with None as first index."""
        self.heap = [None]

        if isinstance(iterable, bool):
            raise TypeError("Heap can only be instantiated with a list, "
                            "tuple or nothing.")

        if iterable:
            if not isinstance(iterable, (tuple, list)):
                raise TypeError("Heap can only be instantiated with a list, "
                                "tuple or nothing.")
            elif all(isinstance(num, int) for num in iterable):
                self.iterable = iterable
                for i in self.iterable:
                    self.push(i)
            else:
                raise TypeError("Heap only accepts numbers")

    def _prioritize_after_push(self, val):
        """Prioritize heap order after push if necessary."""
        child_idx = self.heap.index(val)
        parent_idx = child_idx // 2
        while self.heap[child_idx - 1]:
            parent_val = self.heap[parent_idx]
            child_val = self.heap[child_idx]

            if parent_idx == child_val:
                raise ValueError("Heap only accepts unique values")

            if parent_val > child_val:
                break

            self.heap[child_idx] = parent_val
            self.heap[parent_idx] = child_val
            child_idx = self.heap.index(child_val)
            parent_idx = child_idx // 2

    def push(self, val):
        """Push value into the heap."""
        if not isinstance(val, (str, int, float)):
            raise TypeError("Value must be a number or a string")

        if len(self.heap) == 2 and val == self.heap[1]:
            raise ValueError("Heap only accepts unique values")

        self.heap.append(val)

        if len(self.heap) > 2:
            self._prioritize_after_push(val)

    def _greatest_child_idx(self, parent_idx):
        """Return index of greatest child value if index exists."""
        left_idx = parent_idx + parent_idx
        right_idx = parent_idx + parent_idx + 1

        try:
            self.heap[left_idx]
        except IndexError:
            return None

        try:
            self.heap[right_idx]
        except IndexError:
            return left_idx

        if self.heap[left_idx] > self.heap[right_idx]:
            return left_idx
        return right_idx

    def _prioritize_after_pop(self, val):
        """After pop, reprioritze heap order."""
        parent_idx = self.heap.index(val)
        child_idx = self._greatest_child_idx(parent_idx)

        while child_idx:
            parent_val = self.heap[parent_idx]
            child_val = self.heap[child_idx]
            if parent_val > child_val:
                break
            self.heap[child_idx] = parent_val
            self.heap[parent_idx] = child_val
            parent_idx = child_idx
            child_idx = self._greatest_child_idx(parent_idx)

    def pop(self):
        """Pop value from top of the heap."""
        if len(self.heap) == 1:
            raise IndexError("Empty heap, nothing to pop")

        if len(self.heap) == 2:
            return self.heap.pop()

        root_val = self.heap[1]
        tail_val = self.heap.pop()
        self.heap[1] = tail_val
        self._prioritize_after_pop(tail_val)
        return root_val
