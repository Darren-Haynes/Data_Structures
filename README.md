# Data Structures

### Binary search tree implementation for the Codefellows Python 401 Course

#### Big 0 Notation

- ***__Instantiating an empty tree__ = O(1)
  It is constant time. A tree object is created nothing more.


- __insert()__ = O(n))
 Since this not a balanced binary tree the time complexity is `0(n)`. In the
 case that you have a completey unbalanced tree that is made up of all
 left children or all right children then each node will be checked.


- __depth()__ = O(n)
  This utilizes a recursive function that checks every node in the tree once.


- __search()__ = O(n)
  Since this is not a balanced every node in the tree may need to be searched
  to find the value.


- __balance()__ = O(n)
  This utilizes the depth function to carry out its main task. All nodes are
  checked except for the root node.
