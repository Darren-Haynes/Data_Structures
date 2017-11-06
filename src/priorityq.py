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

        self.val = val
        self.priority = priority



