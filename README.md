# Data Structures

### Hash Table implementation for the Codefellows Python 401 Course

#### Big 0 Notation

- __Instantiating an empty hash table__ = O(1))
  It is constant time. A hash table object is created nothing more.


- ___additive()__ = O(n))
  The additive hash method is an `O(n)` operation. `n` being the number of words in the hash that need to be looped over.


- ___elf()__ = O(n)
The elf hash is also an `O(n)` operation. It contains a single for loop that also iterates over the number of keys in the given string that needs to be hashed.


- ___key_exists()__ = O(n)
  `O(n)` is the worst case scenario if there is a bucket that contains 2 of more key/value pairs. If the bucket contains just 1 key/pair or zero, then its `O(1)`.


- __get()__ = O(n)
  This utilizes the depth function to carry out its main task. All nodes are
  checked except for the root node.

- __create_random_table()__ = 
