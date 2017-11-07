"""."""


class PriorityQ(object):
    """."""

    def __init__(self):
        """."""
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
        """."""
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


