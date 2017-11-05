# Data Structures

### Binary heap implementation for the Codefellows Python 401 Course

#### Implentation
The python list is used to store the values of the binary heap. Index 0 of the list is reserved for the python "None" object. This provides 2 advantages:
- 1: Indexing of the the first value in the heap is at index 1 `self.heap[1]`. This makes for some easier math and in my opinion - code that is easier to read.
- 2: When pushing to the heap, if a value bubbles all the way to the top of the heap, it 'bumps' into "None" and sees that there are no more parents to compare and swap with. The caveat to this, however, is that "None" in python 3 functions a little differently to "None" in python 2. You cannot compare a number with "None" in python 3, it will raise a TypeError. In python 2 you CAN compare a number with None, and regardless whether that number is postive, 0 or negative it will always be greater than "None". This left me with an hour of debugging to figure out why some of the tests were failing in python 2. I won't forget this python 2 and Python 3 difference again any time soon.

#### Big 0

- ***__Instantiating an empty binary heap__****** = O(1)
  It is constant time.

- __Instantiating a list with an iterable__ = O(n)
  The `n` refers to how many numbers are in the iterable.

- __Push()__ = O(log(n))
  Best case is `O(1)` if there are no values in the heap yet. It's constant time
  since it does not have to check itself against a parent value. It is simply
  place into the list. Worst case is `O(log(n))`. Each time the child value
  checks with the parent value and needs to swap it cuts the amount of
  traversal through the heap in half.

- __Pop()__ = O(log(n))
  Essentially this is push in reverse and is this `O(log(n))`
