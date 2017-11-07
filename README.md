# Data Structures

### Priority Queue implementation for the Codefellows Python 401 Course

#### Implentation
A python dictionary is used to store priorities and their values. The values take the form of a python list.  For example a Priority Queue with 3 priorities of `-2`, `0` and `4` that contain some values would look like this:
```
{
    -2: ['a', 'b', 'c'],
    0: ['bing', 'bang'],
    4: [1001]
}
```
#### A few things to note:
- If there are no priorities the dictionary will be empty.
- A priority cannot exist if there are no values. Thus if a priority has a single value, and that value is removed (popped), then the priority will be deleted.

#### Yo Big 0

- ***__Instantiating an empty Priority Queue__ = O(1)
  It is constant time. An empty dict is created and a variable `self_highest`
  is set to `False`. All constant time operations


- __Insert()__ = O(1)
  A dictionary key: value pair is either created or an existing key's value is
  updated. The `self_highest` variable is simply set to the new priority if the
  new priority is greater than the present highest priority. These are all
  constant time operations.

- __Pop()__ = O(n)
  The python built-in `max` method is used to get the highest priority from the
  dictionary. This I believe is an `O(n)` operation, since it has to loop the
  dictionary keys in some way to find the priority key that is the greatest
  number.

- __Peek()__ = O(1)
  The dictionary get method is used to find the priority key we are looking
  for - this is an O(1) operation.
