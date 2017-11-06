"""."""


class PriorityQ(object):
    """."""

    def __init__(self):
        """."""
        self.queue = {0: []}
        self._highest2 = [0, 0]
        self._lowest2 = [0, 0]

    def insert(self, val, priority=0):
        """."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")

        if priority in self.queue:
            self.queue[priority].append(val)
        else:
            self.queue[priority] = [val]
            if priority > self._highest2[1]:
                self._highest2[0], self._highest2[1] = self._highest2[1], priority
            if priority < self._lowest2[1]:
                self._lowest2[0], self._lowest2[1] = self._lowest2[1], priority
        return True

    def pop(self):
        """."""
        popped = self.queue[self._highest][-1].pop(0)

