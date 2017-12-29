"""Implement a Priority Queue."""


class PriorityQ(object):
    """Priority Queue Class."""

    def __init__(self):
        """Instantiate an empty queue."""
        self.queue = {}
        self._highest = False
        self._lowest = 0

    def insert(self, val, priority=None):
        """Insert a value into the queue."""

        if priority is None:
            priority = self._lowest

        if not isinstance(priority, (int, float)):
            raise TypeError("Priority must be an number")

        if priority in self.queue:
            self.queue[priority].append(val)
            return

        if priority < self._lowest:
            self._lowest = priority
        elif priority > self._highest:
            self._highest = priority

        self.queue[priority] = [val]
        return

    def pop(self):
        """Pop highest priority value from the q."""
        if not self.queue:
            raise IndexError("Empty queue, nothing to pop")

        popped = self.queue[self._highest].pop(0)
        if not self.queue[self._highest]:
            del self.queue[self._highest]
            try:
                self._highest = max(self.queue, key=int)
            except ValueError:
                self._highest = 0
        return popped

    def peek(self):
        """See what the highest priority value is in the q."""
        if not self.queue:
            return
        return self.queue[self._highest][0]
