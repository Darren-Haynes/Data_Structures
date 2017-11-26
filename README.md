# Data Structures

### Weighted directed graph implementation for the Codefellows Python 401 Course

#### Implentation
A python dictionary is used to store the nodes. The key is name of the node,
the value is the node it points to. Example of the graph data:
```
{
    'A': ['B', 'C', 'D'],
    B: ['C'],
    C: ['D', 'E'].
    D: [],
    E: []
}
```
#### A few things to note:
- 2 nodes never point back to each other. But one node can point to multiple
  nodes.
- A node can exist without pointing to another node, or having another node
  point to it. It can stand alone.

#### Yo Big 0

- ***__Instantiating an empty graph__ = O(1)
  It is constant time. An emtpy dict is created, that's it.


- __add_node()__ = O(1)
 This method just uses the dict setdefault method.


- __add_edge()__ = O(n)
  There are several things happening in this method and they are all `O(1)`
  except for the python list built in method `is item in list` which is `O(n)`

- __nodes()__ = O(n)
  The method turns the keys of a dict into a list.


- __edges()__ = O(n^2)
  There is a double for loop in this method.


- __del_node()__ = O(1)
  This method is very efficient. It uses to dict methods `if key in dict` and
  `del key in dict`. Both these dict methods are `O(1)`.


- __del_edge()__ = O(n)
  Two list methods are utilised: `value in list` and `remove`. These are both
  `O(n)` operations. They are used independantly of each other, thus we do not
  get `O(n^2)`.


- __has_node()__ = O(1)
  This method is simple and simply returns the boolean output of the dict method `key
  in dict`.


- __adjacent()__ = O(n)
  The adjacent method makes use of the `value in list` method which is an
  `O(n)` operation.


- __breadth_first_traversal()__ = O(n^2)
  The bottleneck in this method is the for loop nested inside the while loop.


- __depth_first_traversal()__ = O(n^2)
  This function has an additional loop in contrast to the
  `breadth_first_traversal()` method. There is a for loop nested in a while
  loop, however, the list `reversed` built-in method is applied as part of the
  for loop. This creates a whopping `O(n^3)`
