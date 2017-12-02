"""A Hash Table."""


class HashTable(object):
    """Hash Table."""


    def __init__(self, size=6, hash_type='additive'):
        """Instantiate empty hash table."""

        hash_types = {'additive': self._additive}
        if hash_type not in hash_types:
            raise ValueError("Hashing type doesn't exist")

        self.hash_type = hash_types[hash_type]
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _additive(self, word):
        """Additive hash. Boo."""

        hash = 0
        for char in word:
            hash += ord(char)
        return hash

    def set_table(self, key, value):
        """Put value in hash table."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")

        hash = self.hash_type(key)
        idx = hash % self.size
        self.table[idx].append((key, value))

    def get(self, key):
        """Get value from table via key."""
        if len(self.table[idx]) == 0:
            raise KeyError("Key doesn't exist")

        hash = self.hash_type(key)
        idx = hash % self.size

        if len(self.table[idx]) == 1:
            return self.table[idx][0][1]
        else:
            pass



