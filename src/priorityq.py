"""."""


class PriorityQ(object):
    """."""

    def __init__(self):
        """."""
        self.queue = {0: []}
        self._highest = 0
        self._lowest = 0

    def insert(self, val, priority=0):
        """."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")

        if priority in self.queue:
            self.queue[priority].append(val)
        else:
            self.queue[priority] = [val]
            if priority > self._highest:
                self._highest = priority
            if priority < self._lowest:
                self._lowest = priority
        return True

    def pop(self):
        """."""
        try:
            popped = self.queue[self._highest].pop(0)
        except IndexError:
            return "Empty queue, nothing to pop"

        if not self.queue[self._highest] and self._highest:
            del self.queue[self._highest]
            self._highest = max(self.queue, key=int)
        return popped


