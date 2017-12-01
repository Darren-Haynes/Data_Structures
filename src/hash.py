"""A Hash Table."""


class HashTable(object):
    """Hash Table."""

    def __init__(self, size=6, hash_type='additive'):
        """Instantiate empty hash table."""
        self.table = []
        for i in range(size):
            self.table.append([])

    def _additive(self, word):
        """Additive hash. Boo."""

        hash = 0
        for char in word:
            hash += ord(char)

        return hash
