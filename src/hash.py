"""A Hash Table."""

import random


class HashTable(object):
    """Hash Table."""

    def __init__(self, size=6, hash_type='additive'):
        """Instantiate empty hash table."""
        hash_types = {'additive': self._additive,
                      'elf': self._elf}
        if hash_type not in hash_types:
            raise ValueError("Hashing type doesn't exist")

        self.hash_type = hash_types[hash_type]
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _additive(self, word):
        """Additive hash. Boo."""
        print('ADDIITIVES')
        hash = 0
        for char in word:
            hash += ord(char)
        return hash

    def _elf(self, key):
        print('ELF')
        hash = 0
        x = 0
        for i in range(len(key)):
            hash = (hash << 4) + ord(key[i])
            x = hash & 0xF0000000
            if x != 0:
                hash ^= (x > 24)
            hash &= ~x
        return (hash & 0x7FFFFFFF)

    def key_exists(self, key, idx):
        """If key exists return true, else false."""
        if len(self.table[idx]) == 1:
            if self.table[idx][0][0] == key:
                return True

        if len(self.table[idx]) > 1:
            for pair in self.table[idx]:
                if pair[0] == key:
                    return True

        return False

    def set_table(self, key, value):
        """Put value in hash table."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")

        hash = self.hash_type(key)
        idx = hash % self.size

        if self.key_exists(key, idx):
            raise KeyError("Key already exists")

        self.table[idx].append((key, value))

    def get(self, key):
        """Get value from table via key."""
        hash = self.hash_type(key)
        idx = hash % self.size
        if len(self.table[idx]) == 0:
            raise KeyError("Key doesn't exist")

        if len(self.table[idx]) == 1:
            if self.table[idx][0][1] == key:
                return self.table[idx][0][1]
            else:
                raise KeyError("Key doesn't exist")
        else:
            for pair in self.table[idx]:
                if pair[0] == key:
                    return pair[0]

    def create_random_table(self):
        """Create random table from list of dictionary words."""
        words = []
        with open('words.txt', 'r') as words_file:
            for line in words_file:
                words.append(line.strip())

        keys = random.sample(words, self.size)
        values = random.sample(words, self.size)

        for key, value in zip(keys, values):
            self.set_table(key, value)

    def create_specific_table(self):
        """Create table of length 10 that always has same key, value pairs."""
        self.set_table('aaaaaa', 'betty')
        self.set_table('a', 'bettie')
        self.set_table('apple', 'bob')
        self.set_table('potato', 'fred')
        self.set_table('spinach', 'james')
        self.set_table('sweet potato', 'jenny')
        # self.set_table('squash', 'tammy')
        # self.set_table('kale', 'rob')
        # self.set_table('cucumber', 'rob')
        # self.set_table('tomatoes', 'rob')
