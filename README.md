# Data Structures

A collection of data structures assignments as part of the CodeFellows Python 401 course
[CodeFellows.com](https://codefellows.com "Codefellows Homepage")

<br />

## Data Structure 1: Linked List
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

<br />

## Data Structure 2: Stack
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(1)` | You simply insert something into the head of the stack and now point to the previous head. |
| __pop()__ | `0(1)` | You simply remove the current head and shift the pointer to the new head that replaces it. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push` and `pop` of the list (incremented and decremented) the size is stored in a variable. |

<br />

## Data Structure 3: Doubly Link List
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(1)` | Adding a node changes head to the this node and points new node to previous head node. All simple `0(1) operations|
| __append()__ | `0(1)` | Adding a node changes tail to the this node and points new node to previous tail node. All simple `0(1) operations|
| __shift()__ | `0(1)` | Removes tail and pointers to it. Restablish new tail. All simple `0(1) operations. |
| __pop()__ | `0(1)` | Removes head and pointers to it. Restablish new head. All simple `0(1) operations. |
| __remove()__ | `0(n)` | Worst case is `0(n)` since remove may need to travers the whole list if the item to remove is the last item in list, or not in the list at all. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push`, `pop`, `shift`, `append`, `remove` of the list (incremented and decremented) the size is stored in a variable. |

<br />

## Data Structure 4: Queue
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __enqueue()__ | `0(1)` | You simply insert something into the back of the queue and adjust pointers. |
| __dequeue()__ | `0(1)` | You simply remove the current front and adjust the pointers. |
| __peek()__ | `0(1)` | A simple operation, just check if a node is at the front and return it's value if there is one. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push` and `pop` of the list (incremented and decremented) the size is stored in a variable. |

<br />

## Data Structure 5: Deque
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __appendleft()__ | `0(1)` | You simply insert something into the start of the deque and adjust pointers. |
| __append()__ | `0(1)` | You simply insert something into the end of the deque and adjust pointers. |
| __peekleft()__ | `0(1)` | Just take a peek at the start node. |
| __peek()__ | `0(1)` | Just take a peek at the end node. |
| __pop()__ | `0(1)` | Removes end and pointers to it. All simple `0(1) operations. |
| __popleft()__ | `0(1)` | Removes start and pointers to it. All simple `0(1) operations. |
| __size()__ | `0(1)` | Size is incremented and decremented with each append and pop. So its just accessing a variable containing the size. |

<br />

## Data Structure 5: Priority Queue
Author: Darren Haynes

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __insert()__ | `0(1)` | In this case, the priority queue uses the python dictionary as its datastructure. The insert method utilizes the dictionary `setter` which is an `0(1)` operation. |
| __pop()__ | `0(1)` | This utilizes the python dictionary `get` method which is an `0(1) operations. |
| __peek()__ | `0(1)` | This also utilizes the python dictionary `get` method along with the list `get` (by index) method. Both an `0(1) operations. |

<br />

## Data Structure 6: Max Binary Heap
Author: Darren Haynes

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(log)n` | We are not using standard list iteration with this binary heap. We check for the position of the parent of each child and swap them if need be. The distance between each child and its parent is halfed as we move closer to the head of the heap. This 'halving' gives us a `0(log)n` operation. |
| __pop()__ | `0(log)n` | The initial pop is just `0(1)` and the subsequent reordering of the values has a worst case scenario of `0(log)n`, following the same pattern as the push method. |

<br />

## Data Structures 6 & 7: Simple Graph & Weighted Graph
Author: Darren Haynes

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __add_node()__ | `0(1)` | Adding a node to the graph uses the python dictionary `setter`. |
| __add_edge()__ | `0(1)` | Adding a node to the graph uses the python dictionary `setter`. |
| __nodes()__ | `0(n)` | All the dictionary (graph's) keys are iterated over to return a list of all nodes.
| __edges()__ | `0(n^2)` | To get all the nodes and their edges we need to iterate over the dictionary keys and then iterate over each value (which is a list). Thus we have a nested loop.
| __del_node()__ | `0(n^2)` | To delete the node is a simple `0(1)` operation using the dictionary `del` method. However to delete all the edges pointing to that node we need to iterate over all the other nodes and then iterate over the edges of each of those nodes to find any edges that need to be deleted. This requires a double for a loop and a time complexity of `0(n^2)`.
| __del_edge()__ | `0(n)` | The edge that get's deleted is an element in a list. The list has to reorder itself after the deletion.
| __has_node()__ | `0(1)` | The dictionary `get` method is used to find if node exists in graph.
| __neighbors()__ | `0(1)` | The dictionary `get` method is used to find the list of edges that may be associated with a node.
| __adjacent()__ | `0(1)` | The dictionary `get` method is used several times, but only once at a time.
| __breadth_traversal()__ | `0(n^2)` | Each node has to be iterated over and for each node all of it's edges need to be iterated over.
| __depth_traversal()__ | `0(n^3)` | Each node has to be iterated over and for each node all of it's edges need to be iterated over. However, each time the edges are iterated over, they are reversed first, which is an additional `0(n)` operation, bumping there overall time complexity to `0(n^3)`

<br />

## Data Structures 8: Binary Search Tree
Author: Darren Haynes

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __insert()__ | `0(log)n` | Insert moves through the tree to find the place the inserted value needs to go. With each 'move', the size of the tree is halved. |
| __size()__ | `0(1)` | The size of the tree is incremented and decremented with each insertion and deletion of the node, thus accessing the size is a simple `0(1)`. |
| __depth()__ | `0(n)` | Each node of the tree is traversed once to find the depth. |
| __contains()__ | `0(log)n` | As we check each node to see if matches the value, the size of the tree is cut in half with each check. |
| __balance()__ | `0(n)` | Every node in the tree is checked to establish balance.
| __in_order()__ | `0(n)` | Every node is visited to find the order.

<br />

##  Data Structure 9: Hash Table
Author: Darren Haynes

### Big 0 Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __Instantiating an empty hash table__ | `O(1)` | It is constant time. A hash table object is created nothing more. |
| ___additive()__ | `O(n))` | The additive hash method is an `O(n)` operation. `n` being the number of words in the hash that need to be looped over. |
| ___elf()__ | `O(n)` | The elf hash is also an `O(n)` operation. It contains a single for loop that also iterates over the number of keys in the given string that needs to be hashed. |
| ___key_exists()__ | `O(n)` | `O(n)` is the worst case scenario if there is a bucket that contains 2 of more key/value pairs. If the bucket contains just 1 key/pair or zero, then its `O(1)`. |
| __get()__ | `O(n)` | This utilizes the depth function to carry out its main task. All nodes are checked except for the root node. |

<br />

##  Data Structure 10: Trie
Author: Darren Haynes & [Kavdi Hodgson](https://github.com/kavdi "Kavdi Hodgson Github Profile Page")

### Big 0 Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __Instantiating an empty Trie__ | `O(1))` | It is constant time. A Trie object is created nothing more. |
| ___insert()__ | `O(n^2)` | The inserted string has to be iterated over and then a second loop is opened to begin iterating over the Trie. If a subset of the string is already in the trie then we get a worst case `0(n^2)`. |
| ___contains()__ | `O(n)` | If the string is in the Trie, then worst case is `0(n)` since the whole string within the Trie is iterated over. |
| ___size()__ | `O(1)` | The number of words in the Trie are kept track of when they are inserted and deleted. |
| __remove()__ | `0(n^2` | To remove a string the Trie needs to be traversed to the end of the string, then each value popped back to the beginning of the string. |

<br />

##  Data Structure 10: Bubble Sort
Author: Darren Haynes & [Kavdi Hodgson](https://github.com/kavdi "Kavdi Hodgson Github Profile Page")

### Big 0 Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __Sorting__ | `O(n^2)` | If the list to sort is completely unsorted then worst case scenario is `0(n^2)`. |

<br />

##  Data Structure 11: Quick Sort
Author: Darren Haynes

### Big 0 Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __Sorting__ | `O(n^2)` | If the list to sort is completely unsorted then worst case scenario is `0(n^2)`. |


<br />

##  Data Structure 13: Radix Sort
Author: Darren Haynes & [Kavdi Hodgson](https://github.com/kavdi "Kavdi Hodgson Github Profile Page")

### Big 0 Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __Sorting__ | `O(kn)` | Worst case scenario = `0(n^2)`. |

