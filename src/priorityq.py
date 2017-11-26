"""Implement a Priority Queue."""


class PriorityQ(object):
    """Priority Queue Class."""

    def __init__(self):
        """Instantiate an empty queue."""
        self.queue = {}
        self._highest = False

    def insert(self, val, priority=0):
        """."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")

        if priority in self.queue:
            self.queue[priority].append(val)
        else:
            if not self.queue:
                self._highest = priority
            self.queue[priority] = [val]
            if priority > self._highest:
                self._highest = priority

    def pop(self):
        """Pop highest priority value from the q."""
        if not self.queue:
            return "Empty queue, nothing to pop"

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
            return "Empty queue, nothing to see."
        return self.queue[self._highest][0]


